# Episode 7: Making Choices with Conditionals
# Sample code for decision-making in programs

# ============================================================
# Basic Conditional Statements
# ============================================================

print("=== Basic Conditional Statements ===")

# Simple if statement
inflammation_level = 8

if inflammation_level > 5:
    print(f"High inflammation detected: {inflammation_level}")
    print("Patient needs immediate attention")

# if-else statement
patient_age = 65

if patient_age >= 65:
    print(f"Patient is {patient_age} years old - Senior citizen")
    treatment_priority = "High"
else:
    print(f"Patient is {patient_age} years old - Adult")
    treatment_priority = "Standard"

print(f"Treatment priority: {treatment_priority}")

# if-elif-else statement
inflammation_reading = 3

if inflammation_reading == 0:
    status = "No inflammation"
    action = "Continue monitoring"
elif inflammation_reading <= 2:
    status = "Mild inflammation"
    action = "Apply basic treatment"
elif inflammation_reading <= 5:
    status = "Moderate inflammation"
    action = "Prescribe medication"
else:
    status = "Severe inflammation"
    action = "Emergency intervention required"

print(f"Reading: {inflammation_reading} → {status}")
print(f"Recommended action: {action}")

# ============================================================
# Comparison Operators
# ============================================================

print("\n=== Comparison Operators ===")

# Different comparison operators
temperature = 38.5  # Body temperature in Celsius
normal_temp = 37.0

print(f"Patient temperature: {temperature}°C")
print(f"Temperature > normal: {temperature > normal_temp}")
print(f"Temperature >= 38: {temperature >= 38}")
print(f"Temperature == normal: {temperature == normal_temp}")
print(f"Temperature != normal: {temperature != normal_temp}")
print(f"Temperature < 40: {temperature < 40}")
print(f"Temperature <= 38.5: {temperature <= 38.5}")

# String comparisons
patient_status = "critical"
print(f"\nPatient status: '{patient_status}'")
print(f"Status == 'critical': {patient_status == 'critical'}")
print(f"Status != 'stable': {patient_status != 'stable'}")

# ============================================================
# Logical Operators
# ============================================================

print("\n=== Logical Operators ===")

# Patient assessment using multiple conditions
age = 45
inflammation = 7
fever = True
chronic_condition = False

# AND operator
if age > 60 and inflammation > 5:
    print("High-risk patient: elderly with high inflammation")
else:
    print("Standard risk assessment")

# OR operator
if fever or inflammation > 8:
    print("Patient shows signs of acute condition")
    needs_immediate_care = True
else:
    print("Patient condition appears stable")
    needs_immediate_care = False

# NOT operator
if not chronic_condition:
    print("Patient has no chronic conditions")
    can_use_standard_treatment = True
else:
    print("Patient has chronic conditions - special care needed")
    can_use_standard_treatment = False

# Complex logical expressions
emergency_case = (
    (inflammation > 10)
    or (fever and age > 70)
    or (chronic_condition and inflammation > 5)
)

print(f"Emergency case: {emergency_case}")

if emergency_case:
    print("⚠️  EMERGENCY: Immediate medical attention required")
else:
    print("✓ Regular care protocol applies")

# ============================================================
# Analyzing Inflammation Data with Conditionals
# ============================================================

print("\n=== Inflammation Data Analysis ===")

# Daily inflammation readings for a patient
daily_inflammation = [0, 1, 3, 5, 8, 6, 4, 2, 1, 0, 0, 1, 2, 7, 9, 5, 3, 1]

print("Daily inflammation analysis:")
high_inflammation_days = 0
moderate_inflammation_days = 0
low_inflammation_days = 0

for day, level in enumerate(daily_inflammation, 1):
    if level >= 7:
        category = "HIGH"
        high_inflammation_days += 1
        alert = " ⚠️"
    elif level >= 3:
        category = "MODERATE"
        moderate_inflammation_days += 1
        alert = " ⚡"
    elif level > 0:
        category = "LOW"
        low_inflammation_days += 1
        alert = " ✓"
    else:
        category = "NONE"
        alert = " ○"

    print(f"  Day {day:2d}: {level} ({category}){alert}")

print(f"\nSummary:")
print(f"  High inflammation days: {high_inflammation_days}")
print(f"  Moderate inflammation days: {moderate_inflammation_days}")
print(f"  Low inflammation days: {low_inflammation_days}")

# Treatment recommendation based on pattern
total_days = len(daily_inflammation)
high_percentage = (high_inflammation_days / total_days) * 100

if high_percentage > 30:
    recommendation = "Aggressive treatment needed"
elif high_percentage > 15:
    recommendation = "Enhanced treatment protocol"
elif moderate_inflammation_days > total_days // 2:
    recommendation = "Standard treatment with monitoring"
else:
    recommendation = "Conservative treatment approach"

print(f"Treatment recommendation: {recommendation}")

# ============================================================
# File Processing with Conditionals
# ============================================================

print("\n=== File Processing Decisions ===")

import os

# Simulate checking different data files
data_files = [
    "data/inflammation-01.csv",
    "data/inflammation-02.csv",
    "data/missing-file.csv",
    "data/inflammation-03.csv",
]

processed_files = []
skipped_files = []

for filename in data_files:
    print(f"Checking: {filename}")

    if not os.path.exists(filename):
        print(f"  ✗ File does not exist - skipping")
        skipped_files.append(filename)
        continue

    # Check file size
    file_size = os.path.getsize(filename)

    if file_size == 0:
        print(f"  ✗ File is empty - skipping")
        skipped_files.append(filename)
    elif file_size < 1000:  # Less than 1KB
        print(f"  ⚠️  File is very small ({file_size} bytes) - processing with caution")
        processed_files.append(filename)
    else:
        print(f"  ✓ File looks good ({file_size} bytes) - processing")
        processed_files.append(filename)

print(f"\nProcessing summary:")
print(f"  Files to process: {len(processed_files)}")
print(f"  Files skipped: {len(skipped_files)}")

# ============================================================
# Data Quality Checks
# ============================================================

print("\n=== Data Quality Checks ===")


def assess_data_quality(inflammation_data):
    """Assess the quality of inflammation data."""
    issues = []
    warnings = []

    # Check for negative values
    negative_values = [x for x in inflammation_data if x < 0]
    if negative_values:
        issues.append(f"Negative values found: {negative_values}")

    # Check for extremely high values
    extremely_high = [x for x in inflammation_data if x > 20]
    if extremely_high:
        warnings.append(f"Unusually high values: {extremely_high}")

    # Check for suspicious patterns
    max_value = max(inflammation_data)
    if max_value > 15:
        warnings.append(f"Maximum value ({max_value}) is very high")

    # Check data length
    if len(inflammation_data) != 40:  # Expected 40 days
        issues.append(f"Unexpected data length: {len(inflammation_data)} (expected 40)")

    # Check for flat lines (no variation)
    unique_values = set(inflammation_data)
    if len(unique_values) == 1:
        warnings.append("Data shows no variation (flat line)")

    return issues, warnings


# Test with different data patterns
test_datasets = {
    "Normal data": [0, 1, 2, 3, 2, 1, 0, 1, 2, 1],
    "Suspicious data": [0, 0, 20, 20, 20, 0, 0, 0, 0, 0],
    "Invalid data": [-1, 2, 3, -5, 2, 1, 0, 25, 2, 1],
    "Flat data": [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
}

for dataset_name, data in test_datasets.items():
    print(f"\nAnalyzing {dataset_name}:")
    issues, warnings = assess_data_quality(data)

    if issues:
        print("  🚨 ISSUES FOUND:")
        for issue in issues:
            print(f"    • {issue}")

    if warnings:
        print("  ⚠️  WARNINGS:")
        for warning in warnings:
            print(f"    • {warning}")

    if not issues and not warnings:
        print("  ✅ Data quality looks good")

# ============================================================
# Treatment Decision Algorithm
# ============================================================

print("\n=== Treatment Decision Algorithm ===")


def determine_treatment(patient_data):
    """Determine treatment based on patient data."""
    age = patient_data["age"]
    max_inflammation = patient_data["max_inflammation"]
    avg_inflammation = patient_data["avg_inflammation"]
    has_allergies = patient_data["allergies"]
    chronic_conditions = patient_data["chronic_conditions"]

    treatment = {
        "medication": None,
        "dosage": None,
        "monitoring": None,
        "restrictions": [],
    }

    # Determine medication based on inflammation severity
    if max_inflammation >= 10:
        if has_allergies:
            treatment["medication"] = "Hypoallergenic anti-inflammatory"
        else:
            treatment["medication"] = "Strong anti-inflammatory"
    elif avg_inflammation >= 5:
        treatment["medication"] = "Standard anti-inflammatory"
    elif avg_inflammation >= 2:
        treatment["medication"] = "Mild anti-inflammatory"
    else:
        treatment["medication"] = "Conservative care only"

    # Adjust dosage based on age and conditions
    if age >= 65:
        treatment["dosage"] = "Reduced (senior)"
        treatment["restrictions"].append("Regular liver function monitoring")
    elif age < 18:
        treatment["dosage"] = "Pediatric"
        treatment["restrictions"].append("Parental supervision required")
    else:
        treatment["dosage"] = "Standard adult"

    # Determine monitoring frequency
    if chronic_conditions or max_inflammation >= 8:
        treatment["monitoring"] = "Daily"
    elif avg_inflammation >= 4:
        treatment["monitoring"] = "Every 2 days"
    else:
        treatment["monitoring"] = "Weekly"

    # Additional restrictions based on conditions
    if chronic_conditions:
        treatment["restrictions"].append("Specialist consultation required")

    if has_allergies:
        treatment["restrictions"].append("Allergy protocol active")

    return treatment


# Test the treatment algorithm
test_patients = [
    {
        "name": "John Doe",
        "age": 45,
        "max_inflammation": 12,
        "avg_inflammation": 6.5,
        "allergies": False,
        "chronic_conditions": False,
    },
    {
        "name": "Mary Smith",
        "age": 72,
        "max_inflammation": 8,
        "avg_inflammation": 4.2,
        "allergies": True,
        "chronic_conditions": True,
    },
    {
        "name": "Tommy Johnson",
        "age": 16,
        "max_inflammation": 5,
        "avg_inflammation": 2.8,
        "allergies": False,
        "chronic_conditions": False,
    },
]

print("Treatment recommendations:")
for patient in test_patients:
    treatment = determine_treatment(patient)
    print(f"\nPatient: {patient['name']} (Age: {patient['age']})")
    print(f"  Medication: {treatment['medication']}")
    print(f"  Dosage: {treatment['dosage']}")
    print(f"  Monitoring: {treatment['monitoring']}")

    if treatment["restrictions"]:
        print(f"  Restrictions:")
        for restriction in treatment["restrictions"]:
            print(f"    • {restriction}")

print("\n=== Conditional logic enables smart decision-making! ===")
