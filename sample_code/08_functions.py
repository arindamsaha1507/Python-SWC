# Episode 8: Creating Functions
# Sample code for defining and using functions to organize code

# ============================================================
# Basic Function Definition and Calling
# ============================================================

print("=== Basic Function Definition ===")


def calculate_inflammation_average(inflammation_data):
    """Calculate the average inflammation from a list of readings."""
    total = sum(inflammation_data)
    average = total / len(inflammation_data)
    return average


# Test the function
patient_readings = [2, 3, 1, 4, 6, 3, 2, 1, 0, 2]
avg_inflammation = calculate_inflammation_average(patient_readings)

print(f"Patient readings: {patient_readings}")
print(f"Average inflammation: {avg_inflammation:.2f}")

# ============================================================
# Functions with Multiple Parameters
# ============================================================

print("\n=== Functions with Multiple Parameters ===")


def assess_patient_risk(age, max_inflammation, has_chronic_condition):
    """Assess patient risk level based on multiple factors."""
    risk_score = 0

    # Age factor
    if age >= 65:
        risk_score += 3
    elif age >= 45:
        risk_score += 1

    # Inflammation factor
    if max_inflammation >= 10:
        risk_score += 4
    elif max_inflammation >= 5:
        risk_score += 2
    elif max_inflammation >= 2:
        risk_score += 1

    # Chronic condition factor
    if has_chronic_condition:
        risk_score += 2

    # Determine risk level
    if risk_score >= 7:
        return "High Risk"
    elif risk_score >= 4:
        return "Medium Risk"
    else:
        return "Low Risk"


# Test with different patients
patients = [
    ("Alice", 34, 3, False),
    ("Bob", 67, 8, True),
    ("Carol", 52, 12, False),
    ("David", 28, 1, False),
]

print("Patient risk assessments:")
for name, age, max_inflam, chronic in patients:
    risk = assess_patient_risk(age, max_inflam, chronic)
    print(f"  {name} (age {age}, max inflammation {max_inflam}): {risk}")

# ============================================================
# Functions with Default Parameters
# ============================================================

print("\n=== Functions with Default Parameters ===")


def analyze_inflammation_data(data, threshold=5, include_zeros=True):
    """
    Analyze inflammation data with customizable parameters.

    Parameters:
    - data: list of inflammation readings
    - threshold: level above which inflammation is considered high (default: 5)
    - include_zeros: whether to include zero readings in analysis (default: True)
    """
    # Filter data if needed
    if not include_zeros:
        data = [x for x in data if x > 0]

    if not data:
        return {"error": "No data to analyze"}

    # Calculate statistics
    total_readings = len(data)
    average = sum(data) / total_readings
    maximum = max(data)
    minimum = min(data)
    high_readings = len([x for x in data if x > threshold])

    return {
        "total_readings": total_readings,
        "average": average,
        "maximum": maximum,
        "minimum": minimum,
        "high_readings": high_readings,
        "high_percentage": (high_readings / total_readings) * 100,
    }


# Test with different parameter combinations
test_data = [0, 1, 3, 0, 7, 2, 8, 0, 1, 6, 0, 2]

print("Analysis with default parameters:")
result1 = analyze_inflammation_data(test_data)
print(f"  Average: {result1['average']:.2f}")
print(f"  High readings (>{5}): {result1['high_readings']}")

print("\nAnalysis excluding zeros:")
result2 = analyze_inflammation_data(test_data, include_zeros=False)
print(f"  Average: {result2['average']:.2f}")
print(f"  Total readings: {result2['total_readings']}")

print("\nAnalysis with custom threshold:")
result3 = analyze_inflammation_data(test_data, threshold=3)
print(f"  High readings (>3): {result3['high_readings']}")

# ============================================================
# Functions Returning Multiple Values
# ============================================================

print("\n=== Functions Returning Multiple Values ===")


def get_inflammation_statistics(data):
    """Calculate comprehensive statistics for inflammation data."""
    if not data:
        return None, None, None, None

    mean_value = sum(data) / len(data)
    max_value = max(data)
    min_value = min(data)

    # Calculate standard deviation
    variance = sum((x - mean_value) ** 2 for x in data) / len(data)
    std_dev = variance**0.5

    return mean_value, max_value, min_value, std_dev


# Unpack multiple return values
sample_data = [1, 3, 2, 6, 4, 7, 3, 2, 5, 4]
mean, maximum, minimum, std = get_inflammation_statistics(sample_data)

print(f"Inflammation statistics:")
print(f"  Mean: {mean:.2f}")
print(f"  Maximum: {maximum}")
print(f"  Minimum: {minimum}")
print(f"  Standard deviation: {std:.2f}")

# ============================================================
# Functions as Building Blocks
# ============================================================

print("\n=== Functions as Building Blocks ===")


def load_patient_data(filename):
    """Simulate loading patient data from a file."""
    # In reality, this would use numpy.loadtxt()
    # For demonstration, return simulated data
    simulated_data = [2, 3, 1, 5, 4, 6, 3, 2, 1, 0, 1, 2, 7, 5, 3, 2]
    return simulated_data


def calculate_daily_statistics(data):
    """Calculate daily statistics for patient data."""
    stats = {
        "mean": sum(data) / len(data),
        "max": max(data),
        "min": min(data),
        "range": max(data) - min(data),
    }
    return stats


def classify_inflammation_severity(average_inflammation):
    """Classify inflammation severity based on average."""
    if average_inflammation >= 6:
        return "Severe"
    elif average_inflammation >= 4:
        return "Moderate"
    elif average_inflammation >= 2:
        return "Mild"
    else:
        return "Minimal"


def generate_patient_report(patient_id, filename):
    """Generate a comprehensive patient report."""
    print(f"\n--- Patient Report: {patient_id} ---")

    # Use building block functions
    data = load_patient_data(filename)
    stats = calculate_daily_statistics(data)
    severity = classify_inflammation_severity(stats["mean"])

    print(f"Data source: {filename}")
    print(f"Total readings: {len(data)}")
    print(f"Average inflammation: {stats['mean']:.2f}")
    print(f"Maximum inflammation: {stats['max']}")
    print(f"Inflammation range: {stats['range']}")
    print(f"Severity classification: {severity}")

    return severity


# Generate reports for multiple patients
patient_files = [
    ("Patient_001", "inflammation-01.csv"),
    ("Patient_002", "inflammation-02.csv"),
    ("Patient_003", "inflammation-03.csv"),
]

severity_counts = {"Severe": 0, "Moderate": 0, "Mild": 0, "Minimal": 0}

for patient_id, filename in patient_files:
    severity = generate_patient_report(patient_id, filename)
    severity_counts[severity] += 1

print(f"\n--- Summary ---")
print(f"Patient severity distribution:")
for severity, count in severity_counts.items():
    print(f"  {severity}: {count} patients")

# ============================================================
# Function Documentation and Help
# ============================================================

print("\n=== Function Documentation ===")


def calculate_treatment_dosage(weight, age, severity_score, units="mg"):
    """
    Calculate medication dosage for inflammation treatment.

    Parameters:
    -----------
    weight : float
        Patient weight in kilograms
    age : int
        Patient age in years
    severity_score : int
        Inflammation severity score (1-10)
    units : str, optional
        Dosage units (default: "mg")

    Returns:
    --------
    dict
        Dictionary containing dosage information:
        - 'amount': dosage amount
        - 'units': dosage units
        - 'frequency': doses per day
        - 'warnings': list of warnings

    Examples:
    ---------
    >>> dosage = calculate_treatment_dosage(70, 45, 6)
    >>> print(dosage['amount'])
    420
    """
    warnings = []

    # Base dosage calculation: 6mg per kg
    base_dosage = weight * 6

    # Adjust for severity
    severity_multiplier = 0.5 + (severity_score * 0.1)
    adjusted_dosage = base_dosage * severity_multiplier

    # Age adjustments
    if age >= 65:
        adjusted_dosage *= 0.8  # Reduce for elderly
        warnings.append("Reduced dosage for senior patient")
    elif age < 18:
        adjusted_dosage *= 0.6  # Reduce for children
        warnings.append("Pediatric dosage applied")

    # Determine frequency
    if severity_score >= 8:
        frequency = 3  # Three times daily
    elif severity_score >= 5:
        frequency = 2  # Twice daily
    else:
        frequency = 1  # Once daily

    return {
        "amount": round(adjusted_dosage),
        "units": units,
        "frequency": frequency,
        "warnings": warnings,
    }


# Test the documented function
dosage_info = calculate_treatment_dosage(70, 45, 6)
print(f"Dosage calculation:")
print(f"  Amount: {dosage_info['amount']} {dosage_info['units']}")
print(f"  Frequency: {dosage_info['frequency']} times per day")
if dosage_info["warnings"]:
    print(f"  Warnings: {', '.join(dosage_info['warnings'])}")

# Display function help
print(f"\nFunction documentation:")
print(calculate_treatment_dosage.__doc__)

# ============================================================
# Variable Scope in Functions
# ============================================================

print("\n=== Variable Scope ===")

# Global variables
hospital_name = "General Hospital"
total_patients_treated = 0


def treat_patient(patient_name, inflammation_level):
    """Treat a patient and update global statistics."""
    global total_patients_treated

    # Local variables
    treatment_success = inflammation_level <= 5
    local_message = f"Treating {patient_name} at {hospital_name}"

    print(local_message)

    if treatment_success:
        print(f"  ✓ Treatment successful for {patient_name}")
        total_patients_treated += 1  # Modify global variable
    else:
        print(f"  ⚠️ {patient_name} needs additional treatment")

    return treatment_success


# Test scope example
print(f"Hospital: {hospital_name}")
print(f"Patients treated so far: {total_patients_treated}")

patients_to_treat = [("Alice", 3), ("Bob", 7), ("Carol", 2)]

for name, level in patients_to_treat:
    treat_patient(name, level)

print(f"Total patients successfully treated: {total_patients_treated}")

# ============================================================
# Lambda Functions (Anonymous Functions)
# ============================================================

print("\n=== Lambda Functions ===")


# Regular function
def double_inflammation(x):
    return x * 2


# Equivalent lambda function
double_lambda = lambda x: x * 2

inflammation_readings = [1, 2, 3, 4, 5]
print(f"Original readings: {inflammation_readings}")

# Using map with lambda
doubled_readings = list(map(lambda x: x * 2, inflammation_readings))
print(f"Doubled readings: {doubled_readings}")

# Using filter with lambda
high_readings = list(filter(lambda x: x > 3, inflammation_readings))
print(f"High readings (>3): {high_readings}")

# Sorting with lambda
patient_data = [("Alice", 4.2), ("Bob", 2.1), ("Carol", 6.8), ("David", 1.5)]

# Sort by inflammation level
sorted_by_inflammation = sorted(patient_data, key=lambda patient: patient[1])
print(f"Patients sorted by inflammation:")
for name, level in sorted_by_inflammation:
    print(f"  {name}: {level}")

print("\n=== Functions help organize and reuse code! ===")
print("Benefits of functions:")
print("  • Break complex problems into smaller parts")
print("  • Avoid code repetition")
print("  • Make code easier to test and debug")
print("  • Enable code reuse across projects")
