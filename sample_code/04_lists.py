# Episode 4: Storing Multiple Values in Lists
# Sample code for working with Python lists

# ============================================================
# Creating and Working with Lists
# ============================================================

# Create lists of inflammation data
patient_inflammation_day1 = [0, 0, 0, 0, 0, 1, 1, 0, 0]  # 9 patients, day 1
patient_inflammation_day2 = [1, 1, 2, 1, 3, 0, 1, 2, 1]  # 9 patients, day 2

print("Day 1 inflammation readings:", patient_inflammation_day1)
print("Day 2 inflammation readings:", patient_inflammation_day2)
print("Number of patients:", len(patient_inflammation_day1))

# Lists of filenames to process
data_files = [
    "inflammation-01.csv",
    "inflammation-02.csv",
    "inflammation-03.csv",
    "inflammation-04.csv",
    "inflammation-05.csv",
]

print("\nData files to analyze:", data_files)
print("Total files:", len(data_files))

# ============================================================
# List Indexing and Slicing
# ============================================================

print("\n=== List Indexing ===")

# Access individual elements
print("First patient day 1:", patient_inflammation_day1[0])
print("Third patient day 1:", patient_inflammation_day1[2])
print("Last patient day 1:", patient_inflammation_day1[-1])
print("Second to last patient day 1:", patient_inflammation_day1[-2])

# Access filename elements
print("First file:", data_files[0])
print("Last file:", data_files[-1])

print("\n=== List Slicing ===")

# Get subsets of the list
first_three_patients = patient_inflammation_day1[:3]
last_three_patients = patient_inflammation_day1[-3:]
middle_patients = patient_inflammation_day1[2:6]

print("First three patients:", first_three_patients)
print("Last three patients:", last_three_patients)
print("Patients 3-6:", middle_patients)

# Slice with step
every_other_patient = patient_inflammation_day1[::2]
print("Every other patient:", every_other_patient)

# Slice filenames
first_three_files = data_files[:3]
print("First three files:", first_three_files)

# ============================================================
# Modifying Lists
# ============================================================

print("\n=== Modifying Lists ===")

# Lists are mutable - we can change them
inflammation_readings = [1, 2, 3, 4, 5]
print("Original readings:", inflammation_readings)

# Change a single value
inflammation_readings[2] = 8  # Change third reading
print("After changing index 2:", inflammation_readings)

# Change multiple values
inflammation_readings[1:4] = [7, 9, 6]
print("After changing slice [1:4]:", inflammation_readings)

# ============================================================
# List Methods - Adding and Removing Elements
# ============================================================

print("\n=== Adding Elements ===")

# Start with patient list
patients = ["Patient_001", "Patient_002", "Patient_003"]
print("Initial patients:", patients)

# Add single patient
patients.append("Patient_004")
print("After append:", patients)

# Add multiple patients
new_patients = ["Patient_005", "Patient_006"]
patients.extend(new_patients)
print("After extend:", patients)

# Insert at specific position
patients.insert(1, "Patient_urgent")
print("After insert at position 1:", patients)

print("\n=== Removing Elements ===")

# Remove by value
patients.remove("Patient_urgent")
print("After removing urgent patient:", patients)

# Remove by position
removed_patient = patients.pop(2)  # Remove and return
print("Removed patient:", removed_patient)
print("After pop:", patients)

# Remove last element
last_patient = patients.pop()
print("Last patient removed:", last_patient)
print("Final patient list:", patients)

# ============================================================
# List Operations and Functions
# ============================================================

print("\n=== List Operations ===")

# Mathematical operations
readings_morning = [2, 1, 4, 3, 2]
readings_evening = [3, 2, 5, 4, 1]

print("Morning readings:", readings_morning)
print("Evening readings:", readings_evening)

# Combine lists
daily_readings = readings_morning + readings_evening
print("Combined daily readings:", daily_readings)

# Repeat lists
baseline = [0, 0, 0]
extended_baseline = baseline * 3
print("Extended baseline:", extended_baseline)

# List functions
print("Total inflammation (sum):", sum(daily_readings))
print("Minimum reading:", min(daily_readings))
print("Maximum reading:", max(daily_readings))
print("Number of readings:", len(daily_readings))

# ============================================================
# Nested Lists (Lists of Lists)
# ============================================================

print("\n=== Nested Lists ===")

# Create a 2D structure - patients as rows, days as columns
patient_data = [
    [0, 1, 2, 1, 0],  # Patient 1
    [1, 2, 3, 2, 1],  # Patient 2
    [0, 0, 1, 3, 2],  # Patient 3
    [2, 1, 0, 1, 1],  # Patient 4
]

print("Patient data (nested list):")
for i, patient in enumerate(patient_data):
    print(f"  Patient {i+1}: {patient}")

# Access nested elements
print("Patient 1, Day 3:", patient_data[0][2])
print("Patient 3, Day 1:", patient_data[2][0])

# Get all readings for day 1 (first element of each patient list)
day_1_all_patients = [patient[0] for patient in patient_data]
print("Day 1 for all patients:", day_1_all_patients)

# ============================================================
# Heterogeneous Lists
# ============================================================

print("\n=== Heterogeneous Lists ===")

# Lists can contain different data types
patient_record = [
    "Patient_001",  # string
    45,  # integer (age)
    72.5,  # float (weight)
    True,  # boolean (has inflammation)
    [1, 2, 3, 2, 1],  # list (inflammation readings)
]

print("Patient record:", patient_record)
print("Patient name:", patient_record[0])
print("Patient age:", patient_record[1])
print("Patient weight:", patient_record[2])
print("Has inflammation:", patient_record[3])
print("Inflammation pattern:", patient_record[4])

# ============================================================
# List Comprehensions (Preview)
# ============================================================

print("\n=== List Comprehensions ===")

# Create lists using comprehensions
inflammation_scores = [1, 3, 2, 5, 4, 0, 2, 1, 3]

# Square all values
squared_scores = [score**2 for score in inflammation_scores]
print("Original scores:", inflammation_scores)
print("Squared scores:", squared_scores)

# Filter high inflammation (> 2)
high_inflammation = [score for score in inflammation_scores if score > 2]
print("High inflammation scores:", high_inflammation)

# Create patient IDs
patient_ids = [f"Patient_{i:03d}" for i in range(1, 11)]
print("Generated patient IDs:", patient_ids)

# ============================================================
# Working with File Lists
# ============================================================

print("\n=== File Processing Lists ===")

# File extensions and paths
file_names = ["inflammation-01.csv", "inflammation-02.csv", "inflammation-03.csv"]

# Extract information from filenames
file_numbers = []
for filename in file_names:
    # Extract number from filename like 'inflammation-01.csv'
    number_part = filename.split("-")[1].split(".")[0]  # Get '01' part
    file_numbers.append(int(number_part))

print("File names:", file_names)
print("File numbers:", file_numbers)

# Create full paths
data_directory = "data/"
full_paths = [data_directory + filename for filename in file_names]
print("Full paths:", full_paths)

# ============================================================
# Summary Exercise
# ============================================================

print("\n=== Summary: Grocery List Analogy ===")

# Like a grocery list, we can manage our data analysis tasks
analysis_tasks = [
    "Load inflammation data",
    "Calculate daily means",
    "Find maximum values",
    "Create visualization",
    "Save results",
]

print("Analysis tasks:", analysis_tasks)

# Mark tasks as completed (using boolean flags)
task_status = [True, True, False, False, False]  # First two completed

print("\nTask completion status:")
for task, completed in zip(analysis_tasks, task_status):
    status = "✓ DONE" if completed else "⏳ TODO"
    print(f"  {status}: {task}")

# Count remaining tasks
remaining_tasks = task_status.count(False)
print(f"\nRemaining tasks: {remaining_tasks}")

print("\n=== Lists are powerful tools for organizing data! ===")
