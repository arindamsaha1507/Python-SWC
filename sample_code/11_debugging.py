# Episode 11: Debugging
# Sample code demonstrating debugging techniques and strategies

import os
import sys

# ============================================================
# Understanding and Reading Error Messages
# ============================================================

print("=== Understanding Error Messages ===")


def demonstrate_stack_trace():
    """Demonstrate how to read and understand stack traces."""

    def level_1_function():
        """First level of function calls."""
        print("  Entering level_1_function")
        level_2_function()

    def level_2_function():
        """Second level of function calls."""
        print("  Entering level_2_function")
        level_3_function()

    def level_3_function():
        """Third level where error occurs."""
        print("  Entering level_3_function")
        inflammation_data = [1, 2, 3, 4, 5]
        # This will cause an IndexError
        problematic_value = inflammation_data[10]  # Index out of range
        return problematic_value

    try:
        level_1_function()
    except IndexError as e:
        print("\n📊 Stack Trace Analysis:")
        print("  ✓ Error Type: IndexError")
        print("  ✓ Error occurred in: level_3_function")
        print("  ✓ Called from: level_2_function → level_1_function")
        print("  ✓ Problem: Trying to access index 10 in 5-element list")
        print(f"  ✓ Error message: {e}")


demonstrate_stack_trace()

# ============================================================
# Print Statement Debugging
# ============================================================

print("\n=== Print Statement Debugging ===")


def analyze_patient_data_with_debug(patient_readings):
    """Analyze patient data with debug print statements."""

    print(f"🔍 DEBUG: Starting analysis with {len(patient_readings)} readings")
    print(f"🔍 DEBUG: Raw data: {patient_readings}")

    # Check for empty data
    if not patient_readings:
        print("🔍 DEBUG: Empty data detected - returning early")
        return None

    # Calculate statistics with debugging
    total = 0
    for i, reading in enumerate(patient_readings):
        print(f"🔍 DEBUG: Processing reading {i}: {reading}")
        total += reading
        print(f"🔍 DEBUG: Running total: {total}")

    average = total / len(patient_readings)
    print(f"🔍 DEBUG: Calculated average: {average}")

    # Find maximum with debugging
    max_reading = patient_readings[0]
    max_index = 0

    for i, reading in enumerate(patient_readings):
        print(f"🔍 DEBUG: Comparing {reading} vs current max {max_reading}")
        if reading > max_reading:
            max_reading = reading
            max_index = i
            print(f"🔍 DEBUG: New maximum found: {max_reading} at index {max_index}")

    result = {
        "average": average,
        "maximum": max_reading,
        "max_day": max_index + 1,  # Convert to 1-based day numbering
    }

    print(f"🔍 DEBUG: Final result: {result}")
    return result


# Test with debug output
test_data = [2, 5, 1, 8, 3, 6, 2]
print("Analyzing patient data with debug output:")
result = analyze_patient_data_with_debug(test_data)

# ============================================================
# Using Python Debugger (pdb) Concepts
# ============================================================

print("\n=== Python Debugger Concepts ===")


def simulate_debugger_session():
    """Simulate what happens in a debugger session."""

    print("Simulating debugger commands:")
    print("  > python -m pdb script.py")
    print("  (Pdb) l          # List current code")
    print("  (Pdb) n          # Next line")
    print("  (Pdb) s          # Step into function")
    print("  (Pdb) c          # Continue execution")
    print("  (Pdb) p variable # Print variable value")
    print("  (Pdb) pp variable# Pretty print variable")
    print("  (Pdb) b 25       # Set breakpoint at line 25")
    print("  (Pdb) q          # Quit debugger")


def debuggable_function(inflammation_data):
    """Function designed for debugging demonstration."""

    # Breakpoint would be set here in real debugging
    # import pdb; pdb.set_trace()  # Uncomment to use actual debugger

    print("🐛 Would set breakpoint here in real debugging")
    print("🐛 In debugger, you could inspect variables:")
    print(f"🐛   inflammation_data = {inflammation_data}")

    processed_data = []
    for i, value in enumerate(inflammation_data):
        # Another potential breakpoint location
        print(f"🐛 Processing item {i}: {value}")

        if value < 0:
            print(f"🐛 Found negative value at index {i}: {value}")
            # In debugger, you could examine why this happened
            processed_value = 0  # Fix negative values
        else:
            processed_value = value

        processed_data.append(processed_value)
        print(f"🐛 Processed value: {processed_value}")

    return processed_data


simulate_debugger_session()
print("\nTesting debuggable function:")
test_values = [2, -1, 4, 3, -2, 6]
result = debuggable_function(test_values)
print(f"Result: {result}")

# ============================================================
# Logging for Debugging
# ============================================================

print("\n=== Logging for Debugging ===")

import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)

logger = logging.getLogger(__name__)


def analyze_with_logging(filename):
    """Analyze data with proper logging instead of print statements."""

    logger.info(f"Starting analysis of {filename}")

    try:
        # Simulate file existence check
        if not os.path.exists(filename):
            logger.error(f"File not found: {filename}")
            return None

        logger.debug(f"File exists, proceeding with analysis")

        # Simulate data loading
        logger.debug("Loading inflammation data...")

        # Simulate different scenarios based on filename
        if "corrupt" in filename:
            logger.warning(f"Suspicious patterns detected in {filename}")
            simulated_data = [1, 2, -1, 4, 999, 3]  # Problematic data
        else:
            simulated_data = [2, 3, 1, 4, 5, 3, 2, 1]  # Normal data

        logger.debug(f"Loaded {len(simulated_data)} data points")

        # Validate data
        negative_values = [x for x in simulated_data if x < 0]
        if negative_values:
            logger.warning(
                f"Found {len(negative_values)} negative values: {negative_values}"
            )

        extreme_values = [x for x in simulated_data if x > 50]
        if extreme_values:
            logger.warning(
                f"Found {len(extreme_values)} extreme values: {extreme_values}"
            )

        # Calculate statistics
        average = sum(simulated_data) / len(simulated_data)
        logger.debug(f"Calculated average: {average}")

        maximum = max(simulated_data)
        logger.debug(f"Found maximum: {maximum}")

        logger.info(f"Analysis completed successfully for {filename}")

        return {
            "filename": filename,
            "average": average,
            "maximum": maximum,
            "data_points": len(simulated_data),
            "warnings": len(negative_values) + len(extreme_values),
        }

    except Exception as e:
        logger.error(f"Analysis failed for {filename}: {e}")
        return None


# Test logging
test_files = ["data/inflammation-01.csv", "data/corrupt-data.csv", "data/missing.csv"]

print("Testing analysis with logging:")
for filename in test_files:
    result = analyze_with_logging(filename)
    if result:
        print(f"  ✓ {filename}: average={result['average']:.2f}")

# ============================================================
# Debugging Logic Errors
# ============================================================

print("\n=== Debugging Logic Errors ===")


def buggy_calculate_weekly_average(daily_readings):
    """Function with subtle logic bug - can you spot it?"""

    print(f"🐛 Calculating weekly average for: {daily_readings}")

    # BUG: This logic is incorrect!
    # It should group by weeks, not just take first 7 values
    if len(daily_readings) >= 7:
        week_total = 0
        for i in range(7):  # BUG: Always takes first 7 days
            week_total += daily_readings[i]
            print(f"🐛 Day {i+1}: {daily_readings[i]}, running total: {week_total}")

        weekly_average = week_total / 7
        print(f"🐛 Weekly average: {weekly_average}")
        return weekly_average
    else:
        print("🐛 Not enough data for weekly average")
        return None


def fixed_calculate_weekly_average(daily_readings):
    """Fixed version that properly handles multiple weeks."""

    print(f"✅ Calculating weekly averages for: {daily_readings}")

    weekly_averages = []

    # Process complete weeks
    for week_start in range(0, len(daily_readings), 7):
        week_end = min(week_start + 7, len(daily_readings))

        if week_end - week_start == 7:  # Only process complete weeks
            week_data = daily_readings[week_start:week_end]
            week_average = sum(week_data) / 7
            weekly_averages.append(week_average)
            print(
                f"✅ Week {len(weekly_averages)}: {week_data} → average: {week_average:.2f}"
            )

    print(f"✅ All weekly averages: {weekly_averages}")
    return weekly_averages


# Demonstrate the bug
sample_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]  # 2 weeks of data

print("Testing buggy function:")
buggy_result = buggy_calculate_weekly_average(sample_data)

print("\nTesting fixed function:")
fixed_result = fixed_calculate_weekly_average(sample_data)

print(f"\nComparison:")
print(f"  Buggy result: {buggy_result}")
print(f"  Fixed result: {fixed_result}")

# ============================================================
# Systematic Debugging Approach
# ============================================================

print("\n=== Systematic Debugging Approach ===")


def debug_inflammation_analysis(data, expected_max=20):
    """Systematic approach to debugging data analysis."""

    debug_info = {"step": 0, "issues_found": [], "data_summary": {}}

    # Step 1: Validate input
    debug_info["step"] = 1
    print(f"🔍 Step {debug_info['step']}: Input validation")

    if not isinstance(data, list):
        issue = f"Expected list, got {type(data)}"
        debug_info["issues_found"].append(issue)
        print(f"  ❌ {issue}")
        return debug_info

    if len(data) == 0:
        issue = "Empty data list"
        debug_info["issues_found"].append(issue)
        print(f"  ❌ {issue}")
        return debug_info

    print(f"  ✅ Input is valid list with {len(data)} elements")

    # Step 2: Examine data characteristics
    debug_info["step"] = 2
    print(f"🔍 Step {debug_info['step']}: Data characteristics")

    debug_info["data_summary"]["length"] = len(data)
    debug_info["data_summary"]["sample"] = data[:5]  # First 5 elements

    print(f"  📊 Length: {len(data)}")
    print(f"  📊 Sample: {data[:5]}")
    print(f"  📊 Types: {[type(x).__name__ for x in data[:3]]}")

    # Step 3: Check for data quality issues
    debug_info["step"] = 3
    print(f"🔍 Step {debug_info['step']}: Data quality checks")

    # Check data types
    non_numeric = [i for i, x in enumerate(data) if not isinstance(x, (int, float))]
    if non_numeric:
        issue = f"Non-numeric values at indices: {non_numeric[:5]}"
        debug_info["issues_found"].append(issue)
        print(f"  ⚠️ {issue}")

    # Check for negative values
    negative_indices = [
        i for i, x in enumerate(data) if isinstance(x, (int, float)) and x < 0
    ]
    if negative_indices:
        issue = f"Negative values at indices: {negative_indices[:5]}"
        debug_info["issues_found"].append(issue)
        print(f"  ⚠️ {issue}")

    # Check for extreme values
    numeric_data = [x for x in data if isinstance(x, (int, float))]
    if numeric_data:
        max_value = max(numeric_data)
        if max_value > expected_max:
            issue = (
                f"Extreme value detected: {max_value} (expected max: {expected_max})"
            )
            debug_info["issues_found"].append(issue)
            print(f"  ⚠️ {issue}")

    # Step 4: Perform calculations with validation
    debug_info["step"] = 4
    print(f"🔍 Step {debug_info['step']}: Calculations")

    if numeric_data:
        debug_info["data_summary"]["mean"] = sum(numeric_data) / len(numeric_data)
        debug_info["data_summary"]["max"] = max(numeric_data)
        debug_info["data_summary"]["min"] = min(numeric_data)

        print(f"  📊 Mean: {debug_info['data_summary']['mean']:.2f}")
        print(
            f"  📊 Range: {debug_info['data_summary']['min']} - {debug_info['data_summary']['max']}"
        )
    else:
        issue = "No numeric data available for calculations"
        debug_info["issues_found"].append(issue)
        print(f"  ❌ {issue}")

    # Step 5: Summary
    debug_info["step"] = 5
    print(f"🔍 Step {debug_info['step']}: Summary")

    if debug_info["issues_found"]:
        print(f"  🚨 Found {len(debug_info['issues_found'])} issues:")
        for i, issue in enumerate(debug_info["issues_found"], 1):
            print(f"    {i}. {issue}")
    else:
        print(f"  ✅ No issues found - data appears clean")

    return debug_info


# Test systematic debugging with different data scenarios
test_datasets = [
    ("Clean data", [1, 2, 3, 4, 5, 4, 3, 2, 1]),
    ("With negative", [1, -2, 3, 4, 5]),
    ("With extreme", [1, 2, 3, 100, 5]),
    ("Mixed types", [1, 2, "three", 4, 5]),
    ("Empty data", []),
]

print("Testing systematic debugging approach:")
for name, data in test_datasets:
    print(f"\n{'='*50}")
    print(f"Testing: {name}")
    print("=" * 50)
    debug_result = debug_inflammation_analysis(data)

# ============================================================
# Debugging Best Practices
# ============================================================

print("\n" + "=" * 60)
print("=== Debugging Best Practices ===")
print("=" * 60)

practices = [
    "1. 📖 Read error messages carefully - they contain valuable information",
    "2. 🔍 Understand the stack trace - it shows the path to the error",
    "3. 🐛 Use print statements strategically to trace execution flow",
    "4. 📝 Use logging instead of print for production code",
    "5. 🎯 Start with the smallest possible failing test case",
    "6. 🔬 Use the Python debugger (pdb) for interactive investigation",
    "7. 🧪 Write unit tests to isolate problems",
    "8. ✂️ Comment out code sections to isolate the problem",
    "9. 🔄 Make one change at a time and test frequently",
    "10. 📋 Keep a debugging log of what you've tried",
    "11. 🤝 Explain the problem to someone else (rubber duck debugging)",
    "12. 😴 Take breaks - fresh eyes often spot obvious problems",
]

for practice in practices:
    print(f"  {practice}")

print("\n💡 Remember: Debugging is a skill that improves with practice!")
print("💡 The goal is not just to fix bugs, but to understand why they occurred!")
