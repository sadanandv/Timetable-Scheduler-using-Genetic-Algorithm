# Timetable-Scheduler-using-Genetic-Algorithm

## Overview
This project provides an automated solution for generating optimized academic timetables using genetic algorithms. The system ensures conflict-free scheduling for student groups and instructors, distributing courses across the available time slots while adhering to various constraints.

The solution handles scheduling for different academic years (batches) and generates separate timetables for student groups and instructors. The algorithm ensures even distribution of courses throughout the week, minimizing scheduling conflicts and overloading.

## Genetic Algorithm, for This?
The genetic algorithm used in this project simulates the process of natural selection to generate the best possible timetable. Here's a breakdown of the key steps:

### 1. Initialization:

  - A population of random timetables is generated. Each timetable consists of genes, where each gene represents a combination of a course, student group, teacher, and time slot.
  - 
### 2. Fitness Calculation:

  - Each timetable (chromosome) is evaluated based on several constraints:
    - No time slot conflicts for student groups or instructors.
    - Satisfying the required number of weekly slots per course.
    - Ensuring even distribution of courses across the week.

### 3. Selection:

  - The timetables with the best fitness scores are selected for reproduction.

### 4. Crossover:

  - Two parent timetables are combined to produce offspring, mixing genes from each parent to create new timetables.

### 5. Mutation:

  - Random mutations are introduced by changing the time slot or instructor for a course. This introduces diversity and helps explore new possible solutions.

### 6. Iteration:

  - The algorithm iterates over several generations, selecting, crossing over, and mutating timetables until an optimal solution is found or the maximum number of generations is reached.

## Features

- **Conflict-Free Scheduling**: Ensures no overlap for teachers or student groups, avoiding double bookings.

- **Dynamic Time Slot Allocation**: Courses are spread across the available time slots, ensuring even distribution throughout the week.

- **Custom Time Slots for Different Years**: Schedules are generated based on the available time slots for different academic years (batches).

- **Separate Instructor Schedules**: Generates personalized schedules for each instructor, outputted in a separate Excel file.

- **Genetic Algorithm Optimization**: Uses a genetic algorithm to evolve towards an optimal solution, taking hard and soft constraints into account.

## Project Structure
```bash
├── data/
│   ├── courses.csv           # List of courses with weekly slots and tutorials info
│   ├── instructors.csv       # Instructor details, including courses they can teach
│   ├── sections.csv          # Student group details and courses they are enrolled in
│   ├── time_slots.csv        # Available time slots for each batch year
├── output/
│   ├── timetable.xlsx        # Generated timetable for student groups
│   ├── instructor_schedule.xlsx # Separate schedules for each instructor
├── genetic_algorithm.py      # Core genetic algorithm logic for timetable generation
├── input_output.py           # Handles reading input data and writing output Excel files
├── schedule.py               # Definitions for core classes like StudentGroup, Teacher, Slot, etc.
├── main.py                   # Main script to execute the timetable generation
├── README.md                 # Project documentation
```

## How to Run

### Pre-Requsites
- Python 3.x
- Required Python Libraries: `pandas`, `openpyxl `
Install the dependencies by running:
```bash
pip install pandas openpyxl
```

### Running the Scheduler
1. Place the input data (`courses.csv`, `instructors.csv`, `sections.csv`, and `time_slots.csv`) in the `data/` directory.
2. Run the main script to generate timetables:
```bash
python main.py
```
3. The generated timetables will be saved in the `output/` directory:
- `timetable.xlsx`: Contains the student group timetables.
- `instructor_schedule.xlsx`: Contains the instructor timetables with separate sheets for each instructor.

## Input Files

### `courses.csv`
Defines the list of courses, including the number of weekly slots required and whether a tutorial is required.

```markdown
| CourseCode | CourseName                          | WeeklySlots | RequiresTutorial |
|------------|-------------------------------------|-------------|------------------|
| CS5701     | Foundations of Data Engineering     | 3           | Yes              |
| CS5702     | Explainable AI                      | 3           | No               |
| CS5703     | Machine Learning Optimization Techniques | 2       | Yes              |
| CS5001     | Data Structures and Algorithms      | 4           | Yes              |
| CS5002     | Advanced Databases                  | 3           | No               |

```
### `instructors.csv`
Contains details about the instructors, including the courses they can teach and their teaching limits.

```markdown
| InstructorID | Name                  | MaxTheoryCourses | MaxPracticalCourses | CanTeach                        |
|--------------|-----------------------|------------------|---------------------|---------------------------------|
| I001         | Dr. abc | 2                | 1                   | CS5701, CS5702, CS5703          |
| I002         | Dr. bcd | 2                | 1                   | CS5001, CS5002, CS5702, CS5704  |
| I003         | Dr. efc | 2                | 2                   | CS5003, CS5701, CS5004          |
| I004         | Dr. xyz | 3                | 1                   | CS5703, CS5001, CS5005          |
| I005         | Dr. aabbcc | 2                | 1                   | CS5002, CS5702, CS5004          |

```

### `sections.csv`
Defines the student groups, their batch year, and the subjects they are enrolled in.

```markdown
| SectionID | BatchYear | Discipline | Subjects                          |
|-----------|-----------|------------|-----------------------------------|
| S1_CS_A   | 1         | CS         | CS5701, CS5001, CS5003            |
| S1_CS_B   | 1         | CS         | CS5701, CS5002, CS5004            |
| S2_CS_A   | 2         | CS         | CS5704, CS5001, CS5003            |
| S2_CS_B   | 2         | CS         | CS5703, CS5002, CS5005            |

```

###`time_slots.csv`
Lists the available time slots, specifying the days, times, and the batch year that each slot is available for.

```markdown
| TimeSlotID | Day       | StartTime | EndTime   | IsBreak | BatchYear |
|------------|-----------|-----------|-----------|---------|-----------|
| 1          | Monday    | 08:10     | 09:00     | No      | 1         |
| 2          | Monday    | 09:00     | 09:50     | No      | 1         |
| 3          | Monday    | 10:10     | 11:00     | No      | 1         |
| 4          | Tuesday   | 08:10     | 09:00     | No      | 2         |
| 5          | Tuesday   | 09:00     | 09:50     | No      | 2         |
| 6          | Wednesday | 08:10     | 09:00     | No      | 3         |
| 7          | Wednesday | 09:00     | 09:50     | No      | 3         |
| 8          | Thursday  | 08:10     | 09:00     | No      | 4         |
| 9          | Thursday  | 09:00     | 09:50     | No      | 4         |

```

## Output Files

### `timetable.xlsx`
- Contains the timetable for student groups.
- Each student group has its own sheet listing their schedule with columns for `Day`, `Time`, `Subject`, and `Instructor`.
### `instructor_schedule.xlsx`
- Contains the schedule for each instructor.
- Each instructor has their own sheet, showing the courses they teach, the student groups, and the assigned time slots.

## Version History

### - _v01: Initial Version_
- Timetable Generation: Basic pipeline implemented to generate timetables for classes based on course, instructor, and time slot availability.
- CSV Inputs: Incorporated inputs from courses.csv, instructors.csv, time_slots.csv, and sections.csv.
- Simple Constraints:
  - Courses were assigned to sections according to required weekly slots.
  - Time slots were assigned to avoid clashes between instructors and student groups.
- Output:
  - Timetable was output to timetable.xlsx.
  - One sheet for each student group, listing the classes for each day and time.

### _v02: Multiple Time Slots for Different Years_
- New Feature: Introduced BatchYear in time_slots.csv to handle different time slots for different years.
  - Each student group now gets assigned time slots specific to their batch year.
- Instructor Schedule: Added instructor_schedule.xlsx to output individual schedules for instructors with separate sheets for each instructor.
- CSV Parsing: Modified CSV parsing logic to handle BatchYear and allow filtered time slot selection for the corresponding batch.
- Constraints: Enhanced logic to assign required slots for each course across the week for different classes, adhering to batch-specific slots.

### _v03: Hyperparameter Tuning and Performance Tracking_
- Parameter Tuning: Added support for hyperparameter tuning with the following parameters:
  - Population size
  - Mutation rate
  - Crossover rate
  - Selection method (tournament and roulette wheel)
  - Elitism rate
  - Tournament size
- Convergence Criteria: Implemented convergence threshold, where the algorithm terminates early if no improvement is seen for a set number of generations.
- Output:
  - Plots for best and average fitness across generations were saved into the output/ folder.
  - Generated Excel files (timetable.xlsx and instructor_schedule.xlsx) for the best timetable.

### _v04: Advanced Soft Constraints and Evaluation Metrics_
- Soft Constraints: Incorporated various instructor and student preferences into the fitness evaluation:
  - Max teaching hours per day for instructors.
  - Preference to avoid early/late classes.
  - Grouping of classes for instructors over consecutive days.
  - Breaks between teaching sessions.
  - Specific time preferences for advanced/introductory subjects.
  - Preferences for lab sessions to be scheduled in continuous slots.
- GA Evaluation Metrics:
  - Best Fitness: Quality of the best solution in each generation.
  - Average Fitness: Tracks the overall population's performance.
  - Genetic Diversity: Measures the diversity in the population to avoid premature convergence.
  - Constraint Violations: Counts violations of hard and soft constraints.
  - Convergence Rate: Tracks the number of generations to convergence.
  - Runtime and Memory Usage: Monitors the algorithm's efficiency.
- Plotting:
  - Plots for fitness, diversity, and violations across generations.
  - Saved all plots and performance metrics into the output/ folder.
- Multi-Configuration Testing: Introduced multiple configurations for testing different hyperparameter settings. Results, plots, and metrics are saved in separate folders for each configuration.

### _Upcoming v05: Excel Sheet Formatting Improvements (Planned)_
- Goal: To improve the readability and formatting of the generated Excel sheets (timetable.xlsx and instructor_schedule.xlsx).
- Details: Specific formatting details will be shared to enhance usability.

## Contribution
Feel free to contribute by opening issues or submitting pull requests for improvements or new features.
