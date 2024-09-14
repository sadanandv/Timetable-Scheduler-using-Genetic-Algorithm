import pandas as pd
from schedule import Teacher, Subject, StudentGroup, Slot

def load_inputs():
    courses = pd.read_csv('data/courses.csv')
    instructors = pd.read_csv('data/instructors.csv')
    time_slots = pd.read_csv('data/time_slots.csv')
    sections = pd.read_csv('data/sections.csv')

    teachers = create_teachers(instructors)
    subjects = create_subjects(courses)
    student_groups = create_student_groups(sections, subjects)
    time_slots = create_time_slots(time_slots)  # Ensure BatchYear is handled

    return student_groups, teachers, time_slots


def create_teachers(instructors_df):
    teachers = []
    for _, row in instructors_df.iterrows():
        can_teach_courses = row['CanTeach'].split(',')
        print(f"Teacher: {row['Name']}, CanTeach: {can_teach_courses}")
        teacher = Teacher(
            teacher_id=row['InstructorID'],
            name=row['Name'],
            max_theory_courses=row['MaxTheoryCourses'],
            max_practical_courses=row['MaxPracticalCourses'],
            can_teach=can_teach_courses
        )
        teachers.append(teacher)
    return teachers

def create_subjects(courses_df):
    subjects = []
    for _, row in courses_df.iterrows():
        subject = Subject(
            subject_code=row['CourseCode'],
            name=row['CourseName'],
            weekly_slots=row['WeeklySlots'],
            requires_tutorial=row['RequiresTutorial']
        )
        subjects.append(subject)
    return subjects

def create_student_groups(sections_df, subjects):
    groups = []
    for _, row in sections_df.iterrows():
        group_subjects = [subject for subject in subjects if subject.subject_code in row['Subjects'].split(',')]
        group = StudentGroup(group_id=row['SectionID'], subjects=group_subjects, batch_year=row['BatchYear'])
        groups.append(group)
    return groups


def create_time_slots(time_slots_df):
    time_slots = []
    for _, row in time_slots_df.iterrows():
        time_slot = Slot(
            day=row['Day'],
            start_time=row['StartTime'],
            end_time=row['EndTime'],
            is_break=row['IsBreak'],
            batch_year=row['BatchYear']  # Add batch year
        )
        time_slots.append(time_slot)
    return time_slots

def output_to_excel(timetable, file_name):
    with pd.ExcelWriter(file_name, engine='openpyxl') as writer:
        for gene in timetable.genes:
            # Only write valid rows where all fields (Day, Time, Subject, Teacher) are non-empty
            if gene.time_slot and gene.subject and gene.teacher and gene.student_group:
                df = pd.DataFrame({
                    'Day': [gene.time_slot.day],
                    'Time': [f'{gene.time_slot.start_time}-{gene.time_slot.end_time}'],
                    'Subject': [gene.subject.name],
                    'Teacher': [gene.teacher.name],
                    'Group': [gene.student_group.group_id]
                })
                sheet_name = f'{gene.student_group.group_id}'
                if sheet_name not in writer.sheets:
                    df.to_excel(writer, sheet_name=sheet_name, index=False)
                else:
                    # Append to the existing sheet if it already exists
                    df.to_excel(writer, sheet_name=sheet_name, index=False, header=False, startrow=writer.sheets[sheet_name].max_row)

def output_instructor_schedule(timetable, file_name):
    # Dictionary to hold each instructor's schedule
    instructor_schedules = {}

    for gene in timetable.genes:
        instructor_name = gene.teacher.name
        if instructor_name not in instructor_schedules:
            instructor_schedules[instructor_name] = []
        
        # Append each gene's details to the respective instructor's schedule
        instructor_schedules[instructor_name].append({
            'Day': gene.time_slot.day,
            'Time': f'{gene.time_slot.start_time}-{gene.time_slot.end_time}',
            'Subject': gene.subject.name,
            'Group': gene.student_group.group_id
        })

    # Write to Excel with separate sheets for each instructor
    with pd.ExcelWriter(file_name, engine='openpyxl') as writer:
        for instructor, schedule in instructor_schedules.items():
            df = pd.DataFrame(schedule)
            df.to_excel(writer, sheet_name=instructor, index=False)
