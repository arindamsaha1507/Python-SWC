# Episode 2: Analyzing Patient Data with NumPy
# Sample code for loading and analyzing tabular data

import numpy as np

# ============================================================
# Loading Data
# ============================================================

# Load inflammation data using NumPy
data = np.loadtxt("data/inflammation-01.csv", delimiter=",")

print("Data shape (rows, columns):", data.shape)
print("Data type:", data.dtype)

# Show first few rows
print("\nFirst 5 rows of data:")
print(data[:5])

# Show specific values
print("\nFirst patient, first day:", data[0, 0])
print("First patient, second day:", data[0, 1])
print("Second patient, first day:", data[1, 0])

# ============================================================
# Array Operations and Statistics
# ============================================================

# Calculate statistics across all data
print("\n=== Overall Statistics ===")
print("Minimum inflammation value:", np.min(data))
print("Maximum inflammation value:", np.max(data))
print("Mean inflammation value:", np.mean(data))
print("Standard deviation:", np.std(data))

# Calculate statistics for specific patients (rows)
print("\n=== Patient-specific Statistics ===")
patient_0_data = data[0, :]  # First patient, all days
print("Patient 0 - Min:", np.min(patient_0_data))
print("Patient 0 - Max:", np.max(patient_0_data))
print("Patient 0 - Mean:", np.mean(patient_0_data))

# Calculate statistics for specific days (columns)
print("\n=== Day-specific Statistics ===")
day_0_data = data[:, 0]  # All patients, first day
print("Day 0 - Min:", np.min(day_0_data))
print("Day 0 - Max:", np.max(day_0_data))
print("Day 0 - Mean:", np.mean(day_0_data))

# ============================================================
# Array Slicing and Indexing
# ============================================================

print("\n=== Array Slicing Examples ===")

# Get first 10 patients, first 10 days
subset = data[:10, :10]
print("Subset shape (first 10 patients, first 10 days):", subset.shape)

# Get middle section of data
middle_patients = data[20:30, :]  # Patients 20-29
middle_days = data[:, 10:20]  # Days 10-19
print("Middle 10 patients shape:", middle_patients.shape)
print("Middle 10 days shape:", middle_days.shape)

# Get every other patient
every_other_patient = data[::2, :]
print("Every other patient shape:", every_other_patient.shape)

# ============================================================
# Calculations Across Axes
# ============================================================

print("\n=== Axis-based Calculations ===")

# Calculate daily averages (average across all patients for each day)
daily_means = np.mean(data, axis=0)  # axis=0 means across rows
print("Daily means shape:", daily_means.shape)
print("First 10 daily means:", daily_means[:10])

# Calculate patient averages (average across all days for each patient)
patient_means = np.mean(data, axis=1)  # axis=1 means across columns
print("Patient means shape:", patient_means.shape)
print("First 10 patient means:", patient_means[:10])

# Other statistics across axes
daily_max = np.max(data, axis=0)
daily_min = np.min(data, axis=0)
patient_max = np.max(data, axis=1)
patient_min = np.min(data, axis=1)

print("Day with highest average inflammation:", np.argmax(daily_means))
print("Patient with highest average inflammation:", np.argmax(patient_means))

# ============================================================
# Working with Multiple Data Files
# ============================================================

print("\n=== Comparing Multiple Files ===")

# Load additional data files
data_02 = np.loadtxt("data/inflammation-02.csv", delimiter=",")
data_03 = np.loadtxt("data/inflammation-03.csv", delimiter=",")

# Compare shapes
print("File 01 shape:", data.shape)
print("File 02 shape:", data_02.shape)
print("File 03 shape:", data_03.shape)

# Compare overall statistics
print("\nComparison of overall means:")
print("File 01 mean:", np.mean(data))
print("File 02 mean:", np.mean(data_02))
print("File 03 mean:", np.mean(data_03))

# ============================================================
# Array Creation and Manipulation
# ============================================================

print("\n=== Array Creation ===")

# Create arrays with specific values
zeros_array = np.zeros((3, 5))
ones_array = np.ones((2, 4))
range_array = np.arange(0, 10, 2)  # 0, 2, 4, 6, 8

print("Zeros array:\n", zeros_array)
print("Ones array:\n", ones_array)
print("Range array:", range_array)

# Create array from list
inflammation_week = np.array([0, 1, 3, 2, 4, 7, 6])
print("Week inflammation pattern:", inflammation_week)

# ============================================================
# Boolean Indexing
# ============================================================

print("\n=== Boolean Indexing ===")

# Find high inflammation days (> 10)
high_inflammation = data > 10
print("Number of high inflammation readings:", np.sum(high_inflammation))

# Get actual values where inflammation is high
high_values = data[high_inflammation]
print("First 10 high inflammation values:", high_values[:10])

# Find patients with very high inflammation on day 0
day_0_high = data[:, 0] > 5
patients_with_high_day_0 = np.where(day_0_high)[0]
print("Patients with high inflammation on day 0:", patients_with_high_day_0[:5])

print("\n=== Analysis Complete ===")
print("Total data points analyzed:", data.size)
print(
    "Percentage of high inflammation readings:",
    100 * np.sum(high_inflammation) / data.size,
    "%",
)
