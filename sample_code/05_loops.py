# Episode 5: Repeating Actions with Loops
# Sample code for automating repetitive tasks

import os

# ============================================================
# Basic For Loops
# ============================================================

print("=== Basic For Loops ===")

# Loop through a list of inflammation readings
inflammation_readings = [0, 1, 3, 2, 5, 4, 3, 2, 1, 0]

print("Processing inflammation readings:")
for reading in inflammation_readings:
    print(f"  Inflammation level: {reading}")

# Loop with enumeration to get index
print("\nWith patient numbers:")
for patient_num, reading in enumerate(inflammation_readings):
    print(f"  Patient {patient_num + 1}: {reading} inflammation units")

# ============================================================
# Range Function for Loops
# ============================================================

print("\n=== Range Function ===")

# Generate sequences of numbers
print("Days 1-10:")
for day in range(1, 11):
    print(f"  Day {day}")

# Range with step
print("\nEvery other day (1-10):")
for day in range(1, 11, 2):
    print(f"  Day {day}")

# Using range with list indexing
patients = ["Alice", "Bob", "Charlie", "Diana"]
print("\nProcessing patients by index:")
for i in range(len(patients)):
    print(f"  Index {i}: {patients[i]}")

# ============================================================
# Processing Multiple Files
# ============================================================

print("\n=== Processing Multiple Files ===")

# List of inflammation data files
data_files = [
    "inflammation-01.csv",
    "inflammation-02.csv",
    "inflammation-03.csv",
    "inflammation-04.csv",
    "inflammation-05.csv",
]

print("Files to process:")
for filename in data_files:
    print(f"  Processing: {filename}")

    # Check if file exists (simulation)
    full_path = f"data/{filename}"
    if os.path.exists(full_path):
        print(f"    ✓ File found: {full_path}")

        # Simulate reading file size
        try:
            file_size = os.path.getsize(full_path)
            print(f"    File size: {file_size} bytes")
        except:
            print(f"    Could not determine file size")
    else:
        print(f"    ✗ File not found: {full_path}")

# ============================================================
# Accumulating Results
# ============================================================

print("\n=== Accumulating Results ===")

# Calculate total inflammation over multiple days
daily_readings = [2, 3, 1, 4, 5, 3, 2, 1, 0, 1]

total_inflammation = 0
print("Daily inflammation accumulation:")
for day, reading in enumerate(daily_readings, 1):
    total_inflammation += reading
    print(f"  Day {day}: +{reading} (Total: {total_inflammation})")

print(f"Final total inflammation: {total_inflammation}")

# Collect maximum readings for each patient
patient_max_readings = []
patient_daily_data = [
    [1, 2, 3, 2, 1],  # Patient 1
    [0, 1, 4, 2, 0],  # Patient 2
    [2, 3, 1, 3, 2],  # Patient 3
    [1, 1, 2, 4, 1],  # Patient 4
]

print("\nFinding maximum reading for each patient:")
for patient_num, daily_data in enumerate(patient_daily_data, 1):
    max_reading = max(daily_data)
    patient_max_readings.append(max_reading)
    print(f"  Patient {patient_num}: max = {max_reading} from {daily_data}")

print(f"All patient maximums: {patient_max_readings}")

# ============================================================
# Nested Loops
# ============================================================

print("\n=== Nested Loops ===")

# Process inflammation data for multiple patients across multiple days
inflammation_matrix = [
    [0, 1, 2, 1, 0],  # Patient 1
    [1, 2, 3, 2, 1],  # Patient 2
    [0, 0, 1, 3, 2],  # Patient 3
]

print("Processing all patient data:")
for patient_id, patient_data in enumerate(inflammation_matrix):
    print(f"  Patient {patient_id + 1}:")
    for day, inflammation in enumerate(patient_data):
        day_num = day + 1
        if inflammation > 2:
            status = "HIGH"
        elif inflammation > 0:
            status = "MODERATE"
        else:
            status = "NONE"
        print(f"    Day {day_num}: {inflammation} ({status})")

# ============================================================
# Loop Control: Break and Continue
# ============================================================

print("\n=== Loop Control ===")

# Using break to stop early
inflammation_sequence = [1, 2, 3, 8, 4, 2, 1, 0]
print("Looking for dangerous inflammation level (>= 7):")

for day, level in enumerate(inflammation_sequence, 1):
    print(f"  Day {day}: {level}")
    if level >= 7:
        print(f"    ⚠️  DANGER! High inflammation detected on day {day}")
        print("    Stopping analysis for safety")
        break
else:
    print("  Analysis complete - no dangerous levels found")

# Using continue to skip iterations
print("\nProcessing only moderate inflammation (1-3):")
for day, level in enumerate(inflammation_sequence, 1):
    if level == 0:
        continue  # Skip days with no inflammation
    if level > 3:
        continue  # Skip days with high inflammation

    print(f"  Day {day}: {level} (moderate level)")

# ============================================================
# Building File Processing Pipeline
# ============================================================

print("\n=== File Processing Pipeline ===")

# Simulate processing multiple files with error handling
file_list = [
    "inflammation-01.csv",
    "inflammation-02.csv",
    "missing-file.csv",
    "inflammation-03.csv",
]

processed_files = []
failed_files = []

print("Processing file pipeline:")
for filename in file_list:
    print(f"  Processing: {filename}")

    # Check if file exists
    full_path = f"data/{filename}"
    if os.path.exists(full_path):
        # Simulate successful processing
        print(f"    ✓ Successfully processed {filename}")
        processed_files.append(filename)
    else:
        print(f"    ✗ Failed to process {filename} (file not found)")
        failed_files.append(filename)

print(f"\nSummary:")
print(f"  Successfully processed: {len(processed_files)} files")
print(f"  Failed: {len(failed_files)} files")

if failed_files:
    print(f"  Failed files: {failed_files}")

# ============================================================
# While Loops
# ============================================================

print("\n=== While Loops ===")

# Monitor inflammation until it drops to zero
current_inflammation = 5
day = 1

print("Monitoring inflammation until recovery:")
while current_inflammation > 0:
    print(f"  Day {day}: Inflammation level = {current_inflammation}")

    # Simulate treatment effect (inflammation decreases)
    current_inflammation -= 1
    day += 1

    # Safety check to prevent infinite loop
    if day > 10:
        print("  Maximum monitoring period reached")
        break

print(f"  Recovery achieved on day {day}!")

# ============================================================
# Creating Data Summaries
# ============================================================

print("\n=== Data Summary Creation ===")

# Process multiple datasets and create summary
datasets = {
    "inflammation-01.csv": [2.1, 3.5, 1.8, 4.2],  # Simulated daily means
    "inflammation-02.csv": [1.9, 3.1, 2.2, 3.8],
    "inflammation-03.csv": [2.3, 3.7, 1.5, 4.1],
}

print("Dataset summary:")
overall_means = []

for filename, daily_means in datasets.items():
    dataset_mean = sum(daily_means) / len(daily_means)
    max_inflammation = max(daily_means)
    min_inflammation = min(daily_means)

    print(f"  {filename}:")
    print(f"    Mean: {dataset_mean:.2f}")
    print(f"    Max:  {max_inflammation:.2f}")
    print(f"    Min:  {min_inflammation:.2f}")

    overall_means.append(dataset_mean)

# Calculate grand summary
grand_mean = sum(overall_means) / len(overall_means)
print(f"\nGrand mean across all datasets: {grand_mean:.2f}")

# ============================================================
# List Comprehensions (Compact Loops)
# ============================================================

print("\n=== List Comprehensions ===")

# Traditional loop approach
squared_values = []
for x in range(1, 6):
    squared_values.append(x**2)
print("Squared values (traditional loop):", squared_values)

# List comprehension approach
squared_values_comp = [x**2 for x in range(1, 6)]
print("Squared values (comprehension):", squared_values_comp)

# Filter high inflammation values
all_readings = [0, 1, 4, 2, 6, 3, 7, 1, 0, 2]
high_readings = [reading for reading in all_readings if reading > 3]
print("High inflammation readings:", high_readings)

# Generate file names
file_numbers = range(1, 6)
generated_filenames = [f"inflammation-{num:02d}.csv" for num in file_numbers]
print("Generated filenames:", generated_filenames)

print("\n=== Loops make repetitive analysis tasks efficient! ===")
