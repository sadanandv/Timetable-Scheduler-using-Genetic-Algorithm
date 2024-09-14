class Teacher:
    def __init__(self, teacher_id, name, max_theory_courses, max_practical_courses, can_teach):
        self.teacher_id = teacher_id
        self.name = name
        self.max_theory_courses = max_theory_courses
        self.max_practical_courses = max_practical_courses
        self.can_teach = can_teach

class Subject:
    def __init__(self, subject_code, name, weekly_slots, requires_tutorial):
        self.subject_code = subject_code
        self.name = name
        self.weekly_slots = weekly_slots
        self.requires_tutorial = requires_tutorial

class StudentGroup:
    def __init__(self, group_id, subjects, batch_year):
        self.group_id = group_id
        self.subjects = subjects
        self.batch_year = batch_year  # Add batch_year attribute


class Slot:
    def __init__(self, day, start_time, end_time, is_break=False, batch_year=None):
        self.day = day
        self.start_time = start_time
        self.end_time = end_time
        self.is_break = is_break
        self.batch_year = batch_year  # New attribute for batch year


class Chromosome:
    def __init__(self, genes):
        self.genes = genes  # A list of Gene objects
        self.fitness = self.calculate_fitness()

    def calculate_fitness(self):
        fitness = 100  # Start with a base fitness score

        # Hard constraints
        fitness -= self.check_teacher_conflicts()  # Penalty for teacher conflicts
        fitness -= self.check_student_group_conflicts()  # Penalty for student group conflicts

        # Soft constraints
        fitness += self.check_soft_constraints()  # Bonus for satisfying soft constraints
        fitness += self.check_even_distribution()  # Bonus for even workload distribution
        fitness += self.check_subject_spread()  # Bonus for spreading subjects over the week

        return fitness

    def check_teacher_conflicts(self):
        conflicts = 0
        scheduled_slots = {}

        for gene in self.genes:
            key = (gene.teacher.teacher_id, gene.time_slot)
            if key in scheduled_slots:
                conflicts += 1
            else:
                scheduled_slots[key] = gene

        return conflicts * 10  # Penalty for conflicts

    def check_student_group_conflicts(self):
        conflicts = 0
        scheduled_slots = {}

        for gene in self.genes:
            key = (gene.student_group.group_id, gene.time_slot)
            if key in scheduled_slots:
                conflicts += 1
            else:
                scheduled_slots[key] = gene

        return conflicts * 10

    def check_soft_constraints(self):
        bonus = 0

        for gene in self.genes:
            if gene.teacher.name == "Dr. Jiji C V" and "08:10" <= gene.time_slot.start_time <= "12:00":
                bonus += 5  # Bonus for morning slots for this teacher

        return bonus

    def check_even_distribution(self):
        day_workload = {day: 0 for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]}

        for gene in self.genes:
            day_workload[gene.time_slot.day] += 1

        max_workload = max(day_workload.values())
        min_workload = min(day_workload.values())

        if max_workload - min_workload > 2:
            return -10  # Penalize uneven distribution
        return 5  # Bonus for even distribution

    def check_subject_spread(self):
        bonus = 0
        group_slots = {}

        for gene in self.genes:
            if gene.student_group.group_id not in group_slots:
                group_slots[gene.student_group.group_id] = set()
            group_slots[gene.student_group.group_id].add(gene.time_slot.day)

        for days in group_slots.values():
            if len(days) >= 3:  # At least 3 days of the week have classes
                bonus += 10

        return bonus

class Gene:
    def __init__(self, subject, teacher, student_group, time_slot):
        self.subject = subject
        self.teacher = teacher
        self.student_group = student_group
        self.time_slot = time_slot
