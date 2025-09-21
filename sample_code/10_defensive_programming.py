# Episode 10: Defensive Programming
# Sample code for writing reliable, robust programs

import os
import sys

# ============================================================
# Assertions for Internal Consistency Checks
# ============================================================

print("=== Assertions for Internal Consistency ===")


def calculate_patient_bmi(weight, height):
    """Calculate BMI with defensive programming checks."""

    # Pre-conditions: Check input validity
    assert isinstance(
        weight, (int, float)
    ), f"Weight must be a number, got {type(weight)}"
    assert isinstance(
        height, (int, float)
    ), f"Height must be a number, got {type(height)}"
    assert weight > 0, f"Weight must be positive, got {weight}"
    assert height > 0, f"Height must be positive, got {height}"
    assert weight < 1000, f"Weight seems unrealistic: {weight} kg"
    assert height < 3, f"Height seems unrealistic: {height} meters"

    # Calculate BMI
    bmi = weight / (height**2)

    # Post-condition: Check result validity
    assert bmi > 0, f"BMI calculation error: {bmi}"
    assert bmi < 100, f"BMI result seems unrealistic: {bmi}"

    return bmi


# Test BMI calculation with valid data
print("Testing BMI calculation:")
try:
    bmi1 = calculate_patient_bmi(70, 1.75)
    print(f"  ✓ BMI for 70kg, 1.75m: {bmi1:.2f}")

    bmi2 = calculate_patient_bmi(65, 1.68)
    print(f"  ✓ BMI for 65kg, 1.68m: {bmi2:.2f}")

except AssertionError as e:
    print(f"  ✗ Assertion failed: {e}")

# Test with invalid data
print("\nTesting with invalid data:")
invalid_test_cases = [
    (-70, 1.75),  # Negative weight
    (70, 0),  # Zero height
    ("70", 1.75),  # String weight
    (70, 5.0),  # Unrealistic height
]

for weight, height in invalid_test_cases:
    try:
        bmi = calculate_patient_bmi(weight, height)
        print(f"  Unexpected success: {weight}kg, {height}m → BMI {bmi:.2f}")
    except AssertionError as e:
        print(f"  ✓ Correctly caught error: {e}")

# ============================================================
# Pre-conditions and Post-conditions
# ============================================================

print("\n=== Pre-conditions and Post-conditions ===")


def analyze_inflammation_trend(daily_readings):
    """
    Analyze inflammation trend with comprehensive checks.

    Pre-conditions:
    - daily_readings must be a list
    - Must have at least 3 readings
    - All readings must be non-negative numbers

    Post-conditions:
    - Returns a trend classification
    - Trend must be one of: 'improving', 'worsening', 'stable'
    """

    # Pre-condition checks
    assert isinstance(daily_readings, list), "daily_readings must be a list"
    assert (
        len(daily_readings) >= 3
    ), f"Need at least 3 readings, got {len(daily_readings)}"

    for i, reading in enumerate(daily_readings):
        assert isinstance(
            reading, (int, float)
        ), f"Reading {i} must be a number, got {type(reading)}"
        assert reading >= 0, f"Reading {i} must be non-negative, got {reading}"

    # Calculate trend
    first_third = sum(daily_readings[: len(daily_readings) // 3])
    last_third = sum(daily_readings[-len(daily_readings) // 3 :])

    if last_third < first_third * 0.8:  # 20% improvement
        trend = "improving"
    elif last_third > first_third * 1.2:  # 20% worsening
        trend = "worsening"
    else:
        trend = "stable"

    # Post-condition checks
    assert trend in ["improving", "worsening", "stable"], f"Invalid trend: {trend}"

    return trend


# Test trend analysis
test_cases = [
    ("Improving case", [8, 7, 6, 5, 4, 3, 2, 1, 0]),
    ("Worsening case", [1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ("Stable case", [5, 4, 6, 5, 4, 6, 5, 4, 5]),
    ("Short data", [5, 6]),  # Should fail pre-condition
]

print("Testing inflammation trend analysis:")
for case_name, data in test_cases:
    try:
        trend = analyze_inflammation_trend(data)
        print(f"  ✓ {case_name}: {trend}")
    except AssertionError as e:
        print(f"  ✗ {case_name}: {e}")

# ============================================================
# Input Validation and Sanitization
# ============================================================

print("\n=== Input Validation and Sanitization ===")


def safe_load_patient_data(filename, expected_columns=40):
    """
    Safely load patient data with comprehensive validation.
    """

    # Input validation
    if not isinstance(filename, str):
        raise TypeError(f"Filename must be a string, got {type(filename)}")

    if not filename.strip():
        raise ValueError("Filename cannot be empty")

    if not filename.endswith(".csv"):
        raise ValueError(f"Expected CSV file, got {filename}")

    # File existence check
    if not os.path.exists(filename):
        raise FileNotFoundError(f"File not found: {filename}")

    # File size check
    file_size = os.path.getsize(filename)
    if file_size == 0:
        raise ValueError(f"File is empty: {filename}")

    if file_size > 10 * 1024 * 1024:  # 10MB limit
        raise ValueError(f"File too large: {file_size} bytes")

    print(f"Loading file: {filename} ({file_size} bytes)")

    # Simulate loading and validating data
    # In real code, this would use numpy.loadtxt()

    # Simulate data validation
    simulated_rows = 60
    simulated_cols = expected_columns

    # Check data dimensions
    if simulated_cols != expected_columns:
        raise ValueError(f"Expected {expected_columns} columns, got {simulated_cols}")

    print(f"  ✓ Loaded {simulated_rows} patients × {simulated_cols} days")

    # Return simulated successful result
    return {"rows": simulated_rows, "columns": simulated_cols, "filename": filename}


# Test safe loading
test_files = [
    ("data/inflammation-01.csv", 40),
    ("data/nonexistent.csv", 40),
    ("not_csv.txt", 40),
    ("", 40),
    (123, 40),  # Wrong type
]

print("Testing safe file loading:")
for filename, expected_cols in test_files:
    try:
        result = safe_load_patient_data(filename, expected_cols)
        print(f"  ✓ {filename}: {result['rows']}×{result['columns']}")
    except (TypeError, ValueError, FileNotFoundError) as e:
        print(f"  ✗ {filename}: {e}")

# ============================================================
# Unit Testing Concepts
# ============================================================

print("\n=== Unit Testing Concepts ===")


def normalize_inflammation(value, min_val=0, max_val=20):
    """
    Normalize inflammation value to 0-1 scale.

    This function demonstrates testable code design.
    """
    assert isinstance(value, (int, float)), "Value must be numeric"
    assert isinstance(min_val, (int, float)), "min_val must be numeric"
    assert isinstance(max_val, (int, float)), "max_val must be numeric"
    assert max_val > min_val, "max_val must be greater than min_val"

    # Clamp value to valid range
    clamped_value = max(min_val, min(value, max_val))

    # Normalize to 0-1
    normalized = (clamped_value - min_val) / (max_val - min_val)

    assert 0 <= normalized <= 1, f"Normalization failed: {normalized}"

    return normalized


def test_normalize_inflammation():
    """Test cases for normalize_inflammation function."""
    test_cases = [
        # (input, expected_output, description)
        (0, 0.0, "Minimum value"),
        (20, 1.0, "Maximum value"),
        (10, 0.5, "Middle value"),
        (-5, 0.0, "Below minimum (should clamp)"),
        (25, 1.0, "Above maximum (should clamp)"),
    ]

    print("Running unit tests for normalize_inflammation:")
    passed = 0
    total = len(test_cases)

    for input_val, expected, description in test_cases:
        try:
            result = normalize_inflammation(input_val)
            if abs(result - expected) < 0.0001:  # Account for floating point precision
                print(f"  ✓ PASS: {description} ({input_val} → {result})")
                passed += 1
            else:
                print(f"  ✗ FAIL: {description} - Expected {expected}, got {result}")
        except Exception as e:
            print(f"  ✗ ERROR: {description} - {e}")

    print(f"Test results: {passed}/{total} tests passed")
    return passed == total


# Run the tests
all_tests_passed = test_normalize_inflammation()

# ============================================================
# Defensive Data Processing Pipeline
# ============================================================

print("\n=== Defensive Data Processing Pipeline ===")


class DataValidationError(Exception):
    """Custom exception for data validation errors."""

    pass


def defensive_process_inflammation_data(data_files):
    """
    Process multiple inflammation data files with defensive programming.
    """

    # Input validation
    if not isinstance(data_files, list):
        raise TypeError("data_files must be a list")

    if not data_files:
        raise ValueError("data_files list cannot be empty")

    results = {"processed": [], "failed": [], "warnings": [], "total_patients": 0}

    for filename in data_files:
        try:
            # Validate filename
            if not isinstance(filename, str):
                raise DataValidationError(f"Invalid filename type: {type(filename)}")

            # Simulate loading and processing
            print(f"Processing: {filename}")

            # Check file exists (simulation)
            if filename.endswith("missing.csv"):
                raise FileNotFoundError("Simulated missing file")

            # Simulate data quality checks
            if "corrupt" in filename:
                raise DataValidationError("Simulated corrupt data")

            # Simulate suspicious data detection
            if "suspicious" in filename:
                results["warnings"].append(f"{filename}: Suspicious patterns detected")

            # Simulate successful processing
            patient_count = 60  # Simulated
            results["processed"].append(
                {"filename": filename, "patients": patient_count, "status": "success"}
            )

            results["total_patients"] += patient_count
            print(f"  ✓ Processed {patient_count} patients")

        except FileNotFoundError as e:
            error_msg = f"{filename}: File not found"
            results["failed"].append(error_msg)
            print(f"  ✗ {error_msg}")

        except DataValidationError as e:
            error_msg = f"{filename}: {e}"
            results["failed"].append(error_msg)
            print(f"  ✗ {error_msg}")

        except Exception as e:
            error_msg = f"{filename}: Unexpected error - {e}"
            results["failed"].append(error_msg)
            print(f"  ✗ {error_msg}")

    # Final validation of results
    assert isinstance(results["total_patients"], int), "Total patients must be integer"
    assert results["total_patients"] >= 0, "Total patients cannot be negative"

    return results


# Test defensive processing
test_file_list = [
    "data/inflammation-01.csv",
    "data/inflammation-02.csv",
    "data/missing.csv",
    "data/corrupt-data.csv",
    "data/suspicious-patterns.csv",
    "data/inflammation-03.csv",
]

print("Testing defensive data processing:")
try:
    processing_results = defensive_process_inflammation_data(test_file_list)

    print(f"\nProcessing Summary:")
    print(f"  Successfully processed: {len(processing_results['processed'])} files")
    print(f"  Failed: {len(processing_results['failed'])} files")
    print(f"  Warnings: {len(processing_results['warnings'])} files")
    print(f"  Total patients: {processing_results['total_patients']}")

    if processing_results["warnings"]:
        print(f"\nWarnings:")
        for warning in processing_results["warnings"]:
            print(f"    {warning}")

except Exception as e:
    print(f"Pipeline failed: {e}")

# ============================================================
# Contract Programming Example
# ============================================================

print("\n=== Contract Programming ===")


def calculate_treatment_effectiveness(before_readings, after_readings):
    """
    Calculate treatment effectiveness percentage.

    Contract:
    - Requires: Both inputs are non-empty lists of same length
    - Requires: All readings are non-negative numbers
    - Ensures: Returns percentage between -100 and 100
    - Ensures: Negative result means worsening, positive means improvement
    """

    # Pre-conditions (requires)
    assert isinstance(before_readings, list), "before_readings must be a list"
    assert isinstance(after_readings, list), "after_readings must be a list"
    assert len(before_readings) > 0, "before_readings cannot be empty"
    assert len(after_readings) > 0, "after_readings cannot be empty"
    assert len(before_readings) == len(after_readings), "Lists must have same length"

    for i, reading in enumerate(before_readings):
        assert isinstance(
            reading, (int, float)
        ), f"before_readings[{i}] must be numeric"
        assert reading >= 0, f"before_readings[{i}] must be non-negative"

    for i, reading in enumerate(after_readings):
        assert isinstance(reading, (int, float)), f"after_readings[{i}] must be numeric"
        assert reading >= 0, f"after_readings[{i}] must be non-negative"

    # Calculate averages
    before_avg = sum(before_readings) / len(before_readings)
    after_avg = sum(after_readings) / len(after_readings)

    # Calculate effectiveness percentage
    if before_avg == 0:
        # Special case: if before was 0, any after value is infinite change
        effectiveness = (
            0 if after_avg == 0 else -100
        )  # Assume worsening if inflammation appears
    else:
        effectiveness = ((before_avg - after_avg) / before_avg) * 100

    # Post-conditions (ensures)
    assert isinstance(effectiveness, (int, float)), "Result must be numeric"
    assert (
        -200 <= effectiveness <= 200
    ), f"Effectiveness out of reasonable range: {effectiveness}"

    return effectiveness


# Test treatment effectiveness calculation
treatment_tests = [
    ("Good improvement", [8, 9, 7, 8], [3, 2, 4, 3]),
    ("Slight improvement", [5, 6, 5, 4], [4, 5, 4, 3]),
    ("No change", [5, 5, 5, 5], [5, 5, 5, 5]),
    ("Worsening", [2, 3, 2, 1], [4, 5, 6, 5]),
    ("Zero baseline", [0, 0, 0, 0], [1, 2, 1, 0]),
]

print("Testing treatment effectiveness calculation:")
for test_name, before, after in treatment_tests:
    try:
        effectiveness = calculate_treatment_effectiveness(before, after)
        interpretation = (
            "improvement"
            if effectiveness > 0
            else "worsening" if effectiveness < 0 else "no change"
        )
        print(f"  ✓ {test_name}: {effectiveness:.1f}% ({interpretation})")
    except AssertionError as e:
        print(f"  ✗ {test_name}: Contract violation - {e}")

print("\n=== Defensive Programming Principles ===")
print("✓ Use assertions to check invariants and assumptions")
print("✓ Validate all inputs at function boundaries")
print("✓ Check outputs before returning")
print("✓ Fail fast and fail clearly with meaningful messages")
print("✓ Write testable code with clear contracts")
print("✓ Handle edge cases explicitly")
print("✓ Use defensive copies when necessary")
print("✓ Log important events and errors")
