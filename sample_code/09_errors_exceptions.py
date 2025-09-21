# Episode 9: Errors and Exceptions
# Sample code for handling errors gracefully in Python programs

import os

# ============================================================
# Understanding Different Types of Errors
# ============================================================

print("=== Understanding Python Errors ===")

# Syntax Errors (these would prevent the script from running)
# Uncomment to see syntax errors:
# print("Missing closing quote
# if True  # Missing colon
# print(Hello World)  # Missing quotes

print("✓ No syntax errors in this script!")

# ============================================================
# Runtime Errors (Exceptions)
# ============================================================

print("\n=== Runtime Errors ===")

# Example 1: ZeroDivisionError
print("1. Division by zero error:")
try:
    inflammation_average = 100 / 0  # This will cause an error
except ZeroDivisionError:
    print("  ✗ Cannot divide by zero!")
    inflammation_average = 0
    print(f"  Set average to {inflammation_average} instead")

# Example 2: IndexError
print("\n2. Index out of range error:")
patient_readings = [2, 3, 1, 4]
try:
    tenth_reading = patient_readings[10]  # Only 4 elements exist
except IndexError:
    print(
        f"  ✗ Index 10 is out of range for list with {len(patient_readings)} elements"
    )
    print(f"  Last valid index is {len(patient_readings) - 1}")

# Example 3: KeyError
print("\n3. Dictionary key error:")
patient_data = {"name": "Alice", "age": 45, "inflammation": 6.2}
try:
    weight = patient_data["weight"]  # Key doesn't exist
except KeyError:
    print("  ✗ 'weight' key not found in patient data")
    print(f"  Available keys: {list(patient_data.keys())}")

# Example 4: TypeError
print("\n4. Type error:")
try:
    result = "inflammation level: " + 6.2  # Can't add string and float
except TypeError:
    print("  ✗ Cannot concatenate string and number")
    result = "inflammation level: " + str(6.2)
    print(f"  Fixed: {result}")

# ============================================================
# File Handling Errors
# ============================================================

print("\n=== File Handling Errors ===")


def safe_file_loading(filename):
    """Safely load a file with proper error handling."""
    try:
        print(f"Attempting to load: {filename}")

        # Check if file exists
        if not os.path.exists(filename):
            raise FileNotFoundError(f"File {filename} not found")

        # Simulate loading file content
        with open(filename, "r") as file:
            # In real usage, this would be numpy.loadtxt()
            first_line = file.readline().strip()
            print(f"  ✓ File loaded successfully")
            print(f"  First line: {first_line[:50]}...")  # Show first 50 characters
            return True

    except FileNotFoundError as e:
        print(f"  ✗ File error: {e}")
        return False
    except PermissionError:
        print(f"  ✗ Permission denied: Cannot read {filename}")
        return False
    except Exception as e:
        print(f"  ✗ Unexpected error: {e}")
        return False


# Test file loading with different scenarios
test_files = [
    "data/inflammation-01.csv",  # Should exist
    "data/nonexistent-file.csv",  # Should not exist
    "data/inflammation-02.csv",  # Should exist
]

successful_loads = 0
for filename in test_files:
    if safe_file_loading(filename):
        successful_loads += 1

print(f"\nSummary: {successful_loads}/{len(test_files)} files loaded successfully")

# ============================================================
# Handling Calculation Errors
# ============================================================

print("\n=== Calculation Errors ===")


def safe_calculate_statistics(data):
    """Calculate statistics with error handling."""
    try:
        if not data:
            raise ValueError("Cannot calculate statistics for empty data")

        if not all(isinstance(x, (int, float)) for x in data):
            raise TypeError("All data points must be numbers")

        # Calculate statistics
        mean = sum(data) / len(data)
        maximum = max(data)
        minimum = min(data)

        # Calculate standard deviation
        if len(data) > 1:
            variance = sum((x - mean) ** 2 for x in data) / (len(data) - 1)
            std_dev = variance**0.5
        else:
            std_dev = 0

        return {
            "mean": mean,
            "max": maximum,
            "min": minimum,
            "std": std_dev,
            "count": len(data),
        }

    except ValueError as e:
        print(f"  ✗ Value error: {e}")
        return None
    except TypeError as e:
        print(f"  ✗ Type error: {e}")
        return None
    except Exception as e:
        print(f"  ✗ Unexpected calculation error: {e}")
        return None


# Test with different data scenarios
test_datasets = [
    ("Normal data", [1, 2, 3, 4, 5]),
    ("Empty data", []),
    ("Single value", [7]),
    ("Mixed types", [1, 2, "three", 4]),
    ("With negative", [-1, 2, 3, 4, 5]),
]

print("Testing statistical calculations:")
for name, data in test_datasets:
    print(f"\n{name}: {data}")
    result = safe_calculate_statistics(data)

    if result:
        print(f"  ✓ Mean: {result['mean']:.2f}")
        print(f"  ✓ Range: {result['min']} - {result['max']}")
        print(f"  ✓ Std Dev: {result['std']:.2f}")

# ============================================================
# User Input Validation
# ============================================================

print("\n=== User Input Validation ===")


def get_valid_inflammation_reading():
    """Get a valid inflammation reading from user input."""
    max_attempts = 3
    attempt = 0

    while attempt < max_attempts:
        try:
            # Simulate user input (in real usage, use input())
            simulated_inputs = ["not_a_number", "-5", "8.5"]
            user_input = simulated_inputs[attempt]
            print(f"Simulated input: '{user_input}'")

            # Convert to float
            reading = float(user_input)

            # Validate range
            if reading < 0:
                raise ValueError("Inflammation reading cannot be negative")
            if reading > 20:
                raise ValueError("Inflammation reading seems unusually high (>20)")

            print(f"  ✓ Valid reading: {reading}")
            return reading

        except ValueError as e:
            attempt += 1
            if "could not convert" in str(e):
                print(f"  ✗ Please enter a number, not '{user_input}'")
            else:
                print(f"  ✗ {e}")

            if attempt < max_attempts:
                print(f"  Try again ({max_attempts - attempt} attempts remaining)")
            else:
                print("  Maximum attempts reached. Using default value of 0.")
                return 0.0


# Test input validation
reading = get_valid_inflammation_reading()
print(f"Final reading: {reading}")

# ============================================================
# Creating Custom Exceptions
# ============================================================

print("\n=== Custom Exceptions ===")


class InflammationDataError(Exception):
    """Custom exception for inflammation data problems."""

    pass


class PatientNotFoundError(Exception):
    """Custom exception for when a patient is not found."""

    pass


def validate_patient_data(patient_id, inflammation_data):
    """Validate patient data with custom exceptions."""

    # Check patient ID
    if not patient_id or not isinstance(patient_id, str):
        raise PatientNotFoundError("Patient ID must be a non-empty string")

    # Check inflammation data
    if not inflammation_data:
        raise InflammationDataError("No inflammation data provided")

    if len(inflammation_data) != 40:
        raise InflammationDataError(
            f"Expected 40 days of data, got {len(inflammation_data)}"
        )

    # Check for suspicious patterns
    max_value = max(inflammation_data)
    if max_value > 20:
        raise InflammationDataError(
            f"Suspiciously high inflammation value: {max_value}"
        )

    # Check for negative values
    negative_values = [x for x in inflammation_data if x < 0]
    if negative_values:
        raise InflammationDataError(
            f"Negative inflammation values found: {negative_values}"
        )

    return True


# Test custom exceptions
test_cases = [
    ("Patient_001", [1, 2, 3] * 13 + [4]),  # Valid 40-day data
    ("", [1, 2, 3]),  # Invalid patient ID
    ("Patient_002", []),  # No data
    ("Patient_003", [1, 2, 3, 25, 5]),  # Suspicious high value
    ("Patient_004", [1, -2, 3, 4, 5]),  # Negative value
]

print("Validating patient data:")
for patient_id, data in test_cases:
    try:
        validate_patient_data(patient_id, data)
        print(f"  ✓ {patient_id}: Data validation passed")
    except PatientNotFoundError as e:
        print(f"  ✗ {patient_id}: Patient error - {e}")
    except InflammationDataError as e:
        print(f"  ✗ {patient_id}: Data error - {e}")
    except Exception as e:
        print(f"  ✗ {patient_id}: Unexpected error - {e}")

# ============================================================
# The Finally Block
# ============================================================

print("\n=== Finally Block ===")


def process_patient_file(filename):
    """Process patient file with cleanup in finally block."""
    file_handle = None
    try:
        print(f"Opening file: {filename}")

        if not os.path.exists(filename):
            raise FileNotFoundError(f"File {filename} not found")

        # Simulate file processing
        print(f"  Processing data from {filename}")
        # In real code: file_handle = open(filename, 'r')

        # Simulate some processing that might fail
        if "suspicious" in filename:
            raise ValueError("Suspicious data pattern detected")

        print(f"  ✓ Successfully processed {filename}")
        return True

    except FileNotFoundError as e:
        print(f"  ✗ File error: {e}")
        return False
    except ValueError as e:
        print(f"  ✗ Data error: {e}")
        return False
    finally:
        # This always runs, whether there was an error or not
        if file_handle:
            print(f"  Closing file handle for {filename}")
            # file_handle.close()
        print(f"  Cleanup completed for {filename}")


# Test finally block
test_files = [
    "data/inflammation-01.csv",
    "data/nonexistent.csv",
    "data/suspicious-data.csv",
]

for filename in test_files:
    process_patient_file(filename)
    print()

# ============================================================
# Best Practices for Error Handling
# ============================================================

print("=== Error Handling Best Practices ===")


def robust_data_analysis(file_list):
    """Demonstrate robust data analysis with comprehensive error handling."""

    results = {"processed": [], "failed": [], "warnings": []}

    for filename in file_list:
        try:
            # Multiple levels of validation
            if not filename.endswith(".csv"):
                results["warnings"].append(f"{filename}: Not a CSV file")
                continue

            if not os.path.exists(filename):
                results["failed"].append(f"{filename}: File not found")
                continue

            # Simulate data loading and analysis
            print(f"Analyzing {filename}...")

            # Simulate potential errors during analysis
            if "corrupt" in filename:
                raise ValueError("Corrupted data detected")

            # Simulate successful analysis
            analysis_result = {
                "file": filename,
                "patients": 60,
                "mean_inflammation": 5.2,
                "status": "success",
            }

            results["processed"].append(analysis_result)
            print(f"  ✓ Analysis complete")

        except ValueError as e:
            error_msg = f"{filename}: Data error - {e}"
            results["failed"].append(error_msg)
            print(f"  ✗ {error_msg}")

        except Exception as e:
            error_msg = f"{filename}: Unexpected error - {e}"
            results["failed"].append(error_msg)
            print(f"  ✗ {error_msg}")

    return results


# Test robust analysis
test_file_list = [
    "data/inflammation-01.csv",
    "data/inflammation-02.csv",
    "data/corrupt-data.csv",
    "data/not-csv.txt",
    "data/missing-file.csv",
]

print("Robust data analysis:")
analysis_results = robust_data_analysis(test_file_list)

print(f"\nFinal Results:")
print(f"  Successfully processed: {len(analysis_results['processed'])}")
print(f"  Failed: {len(analysis_results['failed'])}")
print(f"  Warnings: {len(analysis_results['warnings'])}")

if analysis_results["failed"]:
    print(f"\nFailed files:")
    for error in analysis_results["failed"]:
        print(f"    {error}")

print("\n=== Error handling makes programs robust and user-friendly! ===")
print("Key principles:")
print("  • Anticipate what can go wrong")
print("  • Handle errors gracefully")
print("  • Provide meaningful error messages")
print("  • Always clean up resources")
print("  • Don't hide errors - log or report them")
