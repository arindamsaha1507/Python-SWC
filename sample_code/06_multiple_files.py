# Episode 6: Analyzing Data from Multiple Files
# Sample code for processing multiple data files systematically

import os
import glob

# ============================================================
# Processing Multiple Files with Loops
# ============================================================

print("=== Processing Multiple Inflammation Files ===")

# Method 1: Using a list of known filenames
filenames = [
    "data/inflammation-01.csv",
    "data/inflammation-02.csv",
    "data/inflammation-03.csv",
]

print("Processing files from list:")
for filename in filenames:
    print(f"  Analyzing: {filename}")
    if os.path.exists(filename):
        print(f"    ✓ File exists")
        # Here we would load and analyze the data
        # data = np.loadtxt(filename, delimiter=',')
        # print(f"    Shape: {data.shape}")
    else:
        print(f"    ✗ File not found")

# Method 2: Using glob to find files automatically
print("\nUsing glob to find files automatically:")
inflammation_files = glob.glob("data/inflammation-*.csv")
inflammation_files.sort()  # Sort for consistent order

print(f"Found {len(inflammation_files)} inflammation files:")
for filename in inflammation_files:
    print(f"  {filename}")

# ============================================================
# File Information Gathering
# ============================================================

print("\n=== Gathering File Information ===")


def analyze_file_info(filename):
    """Get basic information about a file."""
    if os.path.exists(filename):
        size = os.path.getsize(filename)
        return {"exists": True, "size_bytes": size, "size_kb": size / 1024}
    else:
        return {"exists": False}


# Analyze all inflammation files
file_info = {}
for filename in inflammation_files[:5]:  # First 5 files
    info = analyze_file_info(filename)
    file_info[filename] = info

    if info["exists"]:
        print(f"{filename}:")
        print(f"  Size: {info['size_kb']:.1f} KB")
    else:
        print(f"{filename}: NOT FOUND")

# ============================================================
# Simulated Data Analysis Pipeline
# ============================================================

print("\n=== Data Analysis Pipeline ===")


def simulate_data_analysis(filename):
    """Simulate analyzing inflammation data from a file."""
    # This would normally use numpy to load and analyze real data
    # For demonstration, we'll simulate the results

    # Extract file number for simulation
    file_num = filename.split("-")[-1].split(".")[0]
    file_number = int(file_num)

    # Simulate different results based on file number
    simulated_results = {
        "filename": filename,
        "patients": 60,
        "days": 40,
        "mean_inflammation": 6.2 + (file_number * 0.1),  # Slight variation
        "max_inflammation": 18 + file_number,
        "min_inflammation": 0,
        "suspicious_pattern": file_number > 10,  # Files after 10 are "suspicious"
    }

    return simulated_results


# Process multiple files and collect results
all_results = []
print("Analyzing inflammation datasets:")

for filename in inflammation_files[:6]:  # Process first 6 files
    print(f"  Processing: {os.path.basename(filename)}")

    results = simulate_data_analysis(filename)
    all_results.append(results)

    print(f"    Patients: {results['patients']}")
    print(f"    Mean inflammation: {results['mean_inflammation']:.2f}")
    print(f"    Max inflammation: {results['max_inflammation']}")

    if results["suspicious_pattern"]:
        print(f"    ⚠️  SUSPICIOUS: Unusual pattern detected!")

# ============================================================
# Comparing Results Across Files
# ============================================================

print("\n=== Comparing Results Across Files ===")

# Extract specific metrics for comparison
mean_values = [result["mean_inflammation"] for result in all_results]
max_values = [result["max_inflammation"] for result in all_results]
file_names = [os.path.basename(result["filename"]) for result in all_results]

print("Summary comparison:")
print("File Name           | Mean  | Max  | Status")
print("-" * 45)

for i, filename in enumerate(file_names):
    mean_val = mean_values[i]
    max_val = max_values[i]
    status = "SUSPICIOUS" if all_results[i]["suspicious_pattern"] else "NORMAL"
    print(f"{filename:<18} | {mean_val:5.2f} | {max_val:4d} | {status}")

# Find outliers
overall_mean = sum(mean_values) / len(mean_values)
print(f"\nOverall mean inflammation: {overall_mean:.2f}")

outliers = []
for i, mean_val in enumerate(mean_values):
    if abs(mean_val - overall_mean) > 0.5:  # Threshold for outlier
        outliers.append((file_names[i], mean_val))

if outliers:
    print("Potential outlier files:")
    for filename, mean_val in outliers:
        print(f"  {filename}: mean = {mean_val:.2f}")
else:
    print("No significant outliers detected.")

# ============================================================
# Creating File Processing Functions
# ============================================================

print("\n=== File Processing Functions ===")


def get_inflammation_files(directory="data", pattern="inflammation-*.csv"):
    """Get all inflammation files from a directory."""
    search_pattern = os.path.join(directory, pattern)
    files = glob.glob(search_pattern)
    files.sort()
    return files


def process_inflammation_file(filename):
    """Process a single inflammation file and return summary statistics."""
    # Simulate processing (would use numpy in real implementation)
    basename = os.path.basename(filename)

    # Extract file number for simulation
    try:
        file_num = int(basename.split("-")[1].split(".")[0])
    except:
        file_num = 1

    # Simulate reading and calculating statistics
    stats = {
        "file": basename,
        "patients": 60,
        "days": 40,
        "mean": 6.0 + (file_num * 0.15),
        "std": 4.5 + (file_num * 0.05),
        "min": 0,
        "max": 15 + file_num,
    }

    return stats


def analyze_all_files(directory="data"):
    """Analyze all inflammation files in a directory."""
    files = get_inflammation_files(directory)
    results = []

    print(f"Found {len(files)} files to analyze:")

    for filename in files:
        if os.path.exists(filename):
            stats = process_inflammation_file(filename)
            results.append(stats)
            print(f"  ✓ {stats['file']}: mean={stats['mean']:.2f}")
        else:
            print(f"  ✗ {filename}: file not found")

    return results


# Use the functions
print("Using our analysis functions:")
analysis_results = analyze_all_files()

# ============================================================
# Batch Processing with Error Handling
# ============================================================

print("\n=== Batch Processing with Error Handling ===")


def safe_file_analysis(filename):
    """Safely analyze a file with error handling."""
    try:
        # Check if file exists
        if not os.path.exists(filename):
            return {"error": "File not found", "filename": filename}

        # Check file size
        size = os.path.getsize(filename)
        if size == 0:
            return {"error": "Empty file", "filename": filename}

        # Simulate successful analysis
        stats = process_inflammation_file(filename)
        stats["status"] = "success"
        return stats

    except Exception as e:
        return {"error": str(e), "filename": filename}


# Process files with error handling
test_files = [
    "data/inflammation-01.csv",
    "data/inflammation-02.csv",
    "data/nonexistent-file.csv",
    "data/inflammation-03.csv",
]

print("Batch processing with error handling:")
successful_analyses = []
failed_analyses = []

for filename in test_files:
    result = safe_file_analysis(filename)

    if "error" in result:
        print(f"  ✗ {os.path.basename(filename)}: {result['error']}")
        failed_analyses.append(result)
    else:
        print(f"  ✓ {result['file']}: mean={result['mean']:.2f}")
        successful_analyses.append(result)

print(f"\nBatch processing summary:")
print(f"  Successful: {len(successful_analyses)}")
print(f"  Failed: {len(failed_analyses)}")

# ============================================================
# Creating Summary Reports
# ============================================================

print("\n=== Creating Summary Report ===")


def create_analysis_report(results):
    """Create a summary report from analysis results."""
    if not results:
        return "No data to report"

    # Calculate summary statistics
    means = [r["mean"] for r in results]
    maxes = [r["max"] for r in results]

    report = []
    report.append("INFLAMMATION DATA ANALYSIS REPORT")
    report.append("=" * 40)
    report.append(f"Files analyzed: {len(results)}")
    report.append(f"Average mean inflammation: {sum(means)/len(means):.2f}")
    report.append(f"Highest max inflammation: {max(maxes)}")
    report.append(f"Lowest max inflammation: {min(maxes)}")
    report.append("")
    report.append("Individual file results:")

    for result in results:
        report.append(
            f"  {result['file']}: mean={result['mean']:.2f}, max={result['max']}"
        )

    return "\n".join(report)


# Generate and display report
if successful_analyses:
    report = create_analysis_report(successful_analyses)
    print(report)

print("\n=== Multi-file analysis complete! ===")
print("This approach allows us to:")
print("  • Process many files automatically")
print("  • Handle errors gracefully")
print("  • Compare results across datasets")
print("  • Generate summary reports")
