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

```csv
InstructorID,Name,MaxTheoryCourses,MaxPracticalCourses,CanTeach
I001,Dr. Jiji C V,2,1,"CS5701,CS5702,CS5703"
I002,Dr. Sakthi Balan,2,1,"CS5001,CS5002,CS5702,CS5704"
I003,Dr. R. Sujatha,2,2,"CS5003,CS5701,CS5004"
I004,Dr. Priyadarshan Parida,3,1,"CS5703,CS5001,CS5005"
I005,Dr. S. Satyanarayanan,2,1,"CS5002,CS5702,CS5004"
```

### `sections.csv`
Defines the student groups, their batch year, and the subjects they are enrolled in.

```csv
SectionID,BatchYear,Discipline,Subjects
S1_CS_A,1,CS,"CS5701,CS5001,CS5003"
S1_CS_B,1,CS,"CS5701,CS5002,CS5004"
S2_CS_A,2,CS,"CS5704,CS5001,CS5003"
S2_CS_B,2,CS,"CS5703,CS5002,CS5005"
```

###`time_slots.csv`
Lists the available time slots, specifying the days, times, and the batch year that each slot is available for.

```csv
TimeSlotID,Day,StartTime,EndTime,IsBreak,BatchYear
1,Monday,08:10,09:00,No,1
2,Monday,09:00,09:50,No,1
3,Monday,10:10,11:00,No,1
4,Tuesday,08:10,09:00,No,2
5,Tuesday,09:00,09:50,No,2
6,Wednesday,08:10,09:00,No,3
7,Wednesday,09:00,09:50,No,3
8,Thursday,08:10,09:00,No,4
9,Thursday,09:00,09:50,No,4
```

## Output Files

### `timetable.xlsx`
- Contains the timetable for student groups.
- Each student group has its own sheet listing their schedule with columns for `Day`, `Time`, `Subject`, and `Instructor`.
### `instructor_schedule.xlsx`
- Contains the schedule for each instructor.
- Each instructor has their own sheet, showing the courses they teach, the student groups, and the assigned time slots.

## Version History
- _v01_: Initial implementation of the timetable generator using genetic algorithms.
- _v02_: Added separate instructor schedule output and year-specific time slots for batch scheduling.

## Contribution
Feel free to contribute by opening issues or submitting pull requests for improvements or new features.
