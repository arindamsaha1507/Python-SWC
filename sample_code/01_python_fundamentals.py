# Episode 1: Python Fundamentals
# Sample code for variables, data types, and basic operations

# ============================================================
# Variables and Assignment
# ============================================================

# Assigning values to variables
patient_weight = 60.0  # weight in kilograms
patient_age = 45  # age in years
patient_name = "Dr. Smith"
has_inflammation = True

print("Patient name:", patient_name)
print("Patient age:", patient_age)
print("Patient weight:", patient_weight, "kg")
print("Has inflammation:", has_inflammation)

# ============================================================
# Data Types
# ============================================================

# Check the type of variables
print("\nData types:")
print("Type of patient_weight:", type(patient_weight))
print("Type of patient_age:", type(patient_age))
print("Type of patient_name:", type(patient_name))
print("Type of has_inflammation:", type(has_inflammation))

# ============================================================
# Using Variables in Python
# ============================================================

# Variables can change
patient_weight = 62.5  # Patient gained weight
print("\nUpdated weight:", patient_weight, "kg")

# Variables can be used in calculations
bmi = patient_weight / (1.75**2)  # BMI calculation (assuming height 1.75m)
print("Patient BMI:", bmi)

# ============================================================
# Built-in Python Functions
# ============================================================

# Mathematical functions
inflammation_reading = 3.14159
print("\nInflammation reading (raw):", inflammation_reading)
print("Rounded inflammation reading:", round(inflammation_reading, 2))
print("Absolute value:", abs(-5.2))
print("Maximum of readings:", max(2.1, 4.7, 1.8, 5.2))
print("Minimum of readings:", min(2.1, 4.7, 1.8, 5.2))

# String functions
print("\nPatient name length:", len(patient_name))
print("Patient name uppercase:", patient_name.upper())

# ============================================================
# Getting Help
# ============================================================

# You can get help on any function
# Uncomment these lines to see help:
# help(round)
# help(len)

# ============================================================
# Working with Inflammation Data Context
# ============================================================

# Sample inflammation values for one patient over 5 days
day1_inflammation = 0
day2_inflammation = 1
day3_inflammation = 3
day4_inflammation = 1
day5_inflammation = 2

print("\nDaily inflammation readings:")
print("Day 1:", day1_inflammation)
print("Day 2:", day2_inflammation)
print("Day 3:", day3_inflammation)
print("Day 4:", day4_inflammation)
print("Day 5:", day5_inflammation)

# Calculate some basic statistics
total_inflammation = (
    day1_inflammation
    + day2_inflammation
    + day3_inflammation
    + day4_inflammation
    + day5_inflammation
)
average_inflammation = total_inflammation / 5

print("\nTotal inflammation over 5 days:", total_inflammation)
print("Average daily inflammation:", average_inflammation)

# ============================================================
# Variables as Sticky Notes Concept
# ============================================================

# Variables are like sticky notes attached to values
inflammation_reading = 5.2
backup_reading = inflammation_reading  # Both variables point to the same value

print("\nOriginal reading:", inflammation_reading)
print("Backup reading:", backup_reading)

# Change the original
inflammation_reading = 6.1
print("After changing original:")
print("Original reading:", inflammation_reading)
print(
    "Backup reading:", backup_reading
)  # Unchanged because it's a separate "sticky note"
