from genetic_algorithm import genetic_algorithm
from input_output import load_inputs, output_to_excel, output_instructor_schedule

def main():
    student_groups, teachers, time_slots = load_inputs()
    best_timetable = genetic_algorithm(student_groups, teachers, time_slots)
    

    output_to_excel(best_timetable, 'output/timetable.xlsx')
    output_instructor_schedule(best_timetable, 'output/instructor_schedule.xlsx')


if __name__ == "__main__":
    main()