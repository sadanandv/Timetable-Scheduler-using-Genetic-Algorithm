import random
from schedule import Chromosome, Gene

def initialize_population(student_groups, teachers, time_slots, population_size=100):
    population = []

    for _ in range(population_size):
        genes = []
        assigned_slots = {}  # To track assigned slots for each group and teacher

        for group in student_groups:
            for subject in group.subjects:
                required_slots = subject.weekly_slots  # Get the number of slots required for the course

                for _ in range(required_slots):  # Assign the required number of slots
                    eligible_teachers = [t for t in teachers if subject.subject_code in t.can_teach]

                    # Find available slots for both the teacher and the group without conflicts
                    teacher, time_slot = find_available_slot(eligible_teachers, time_slots, assigned_slots, group)

                    if teacher and time_slot:
                        gene = Gene(subject, teacher, group, time_slot)
                        genes.append(gene)
                        # Mark the slot as assigned for both the teacher and the group
                        assigned_slots[(group.group_id, time_slot)] = True
                        assigned_slots[(teacher.teacher_id, time_slot)] = True

        chromosome = Chromosome(genes)  # Automatically calculates fitness when created
        population.append(chromosome)

    return population


def find_available_slot(eligible_teachers, time_slots, assigned_slots, group):
    # Filter time slots by the batch year of the student group
    filtered_time_slots = [slot for slot in time_slots if slot.batch_year == group.batch_year]
    
    days_used = set()  # Track the days that are already used for this group

    for teacher in eligible_teachers:
        for time_slot in filtered_time_slots:
            if time_slot.day not in days_used:
                # Check if the slot is available for both the teacher and the group
                if (group.group_id, time_slot) not in assigned_slots and (teacher.teacher_id, time_slot) not in assigned_slots:
                    days_used.add(time_slot.day)  # Add the day to the used list
                    return teacher, time_slot

    # If no preferred time slot is found, return any available slot
    for teacher in eligible_teachers:
        for time_slot in filtered_time_slots:
            if (group.group_id, time_slot) not in assigned_slots and (teacher.teacher_id, time_slot) not in assigned_slots:
                return teacher, time_slot

    return None, None  # No available slot found


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

def selection(population):
    population.sort(key=lambda x: x.fitness, reverse=True)
    return population[:len(population) // 2]

def crossover(parent1, parent2):
    cut_point = random.randint(0, len(parent1.genes) - 1)
    child1_genes = parent1.genes[:cut_point] + parent2.genes[cut_point:]
    child2_genes = parent2.genes[:cut_point] + parent1.genes[cut_point:]
    return Chromosome(child1_genes), Chromosome(child2_genes)

def mutate(chromosome, time_slots, teachers, mutation_rate=0.1):
    for gene in chromosome.genes:
        if random.random() < mutation_rate:
            gene.time_slot = random.choice(time_slots)
            gene.teacher = random.choice([t for t in teachers if gene.subject.subject_code in t.can_teach])

def genetic_algorithm(student_groups, teachers, time_slots, generations=100):
    population = initialize_population(student_groups, teachers, time_slots)
    for _ in range(generations):
        population = selection(population)
        next_generation = []
        while len(next_generation) < len(population):
            parent1, parent2 = random.choice(population), random.choice(population)
            child1, child2 = crossover(parent1, parent2)
            mutate(child1, time_slots, teachers)
            mutate(child2, time_slots, teachers)
            next_generation.extend([child1, child2])
        population = next_generation
    return max(population, key=lambda x: x.fitness)
