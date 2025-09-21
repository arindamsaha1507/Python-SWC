# Episode 12: Command-Line Programs
# Sample code for creating Python programs that work like Unix command-line tools

import sys
import os
import argparse
from pathlib import Path

# ============================================================
# Basic Command-Line Argument Handling with sys.argv
# ============================================================

print("=== Basic Command-Line Arguments ===")


def demonstrate_sys_argv():
    """Demonstrate basic command-line argument access."""

    print(f"Program name: {sys.argv[0]}")
    print(f"Number of arguments: {len(sys.argv)}")
    print(f"All arguments: {sys.argv}")

    if len(sys.argv) > 1:
        print(f"First argument: {sys.argv[1]}")
    else:
        print("No additional arguments provided")


# Simulate command-line arguments for demonstration
original_argv = sys.argv
sys.argv = ["inflammation_analyzer.py", "data/inflammation-01.csv", "--verbose"]

print("Simulating: python inflammation_analyzer.py data/inflammation-01.csv --verbose")
demonstrate_sys_argv()

# Restore original argv
sys.argv = original_argv

# ============================================================
# Simple Command-Line Data Analyzer
# ============================================================

print("\n=== Simple Command-Line Data Analyzer ===")


def simple_inflammation_analyzer():
    """Simple version using sys.argv directly."""

    # Check if filename was provided
    if len(sys.argv) < 2:
        print("Usage: python script.py <filename>")
        print("Example: python script.py data/inflammation-01.csv")
        sys.exit(1)

    filename = sys.argv[1]

    # Check for optional verbose flag
    verbose = "--verbose" in sys.argv or "-v" in sys.argv

    if verbose:
        print(f"🔍 Verbose mode enabled")
        print(f"🔍 Analyzing file: {filename}")

    # Check if file exists
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)

    # Simulate data analysis
    print(f"Analyzing inflammation data from: {filename}")

    # In real implementation, this would use numpy
    simulated_stats = {
        "patients": 60,
        "days": 40,
        "mean_inflammation": 6.14,
        "max_inflammation": 18,
        "min_inflammation": 0,
    }

    if verbose:
        print(f"🔍 Found {simulated_stats['patients']} patients")
        print(f"🔍 Data spans {simulated_stats['days']} days")

    print(f"Results:")
    print(f"  Mean inflammation: {simulated_stats['mean_inflammation']:.2f}")
    print(f"  Maximum inflammation: {simulated_stats['max_inflammation']}")
    print(f"  Minimum inflammation: {simulated_stats['min_inflammation']}")

    return simulated_stats


# Test simple analyzer
print("Testing simple analyzer:")
sys.argv = ["analyzer.py", "data/inflammation-01.csv", "--verbose"]
try:
    result = simple_inflammation_analyzer()
    print("✓ Analysis completed successfully")
except SystemExit:
    print("✗ Program would exit here")

# ============================================================
# Using argparse for Better Command-Line Interface
# ============================================================

print("\n=== Using argparse for Better CLI ===")


def create_argument_parser():
    """Create and configure argument parser."""

    parser = argparse.ArgumentParser(
        description="Analyze inflammation data from CSV files",
        epilog="Example: python %(prog)s data/inflammation-01.csv --plot --output results.txt",
    )

    # Positional argument (required)
    parser.add_argument("filename", help="CSV file containing inflammation data")

    # Optional arguments
    parser.add_argument(
        "--output",
        "-o",
        help="Output file for results (default: print to stdout)",
        default=None,
    )

    parser.add_argument(
        "--verbose", "-v", action="store_true", help="Enable verbose output"
    )

    parser.add_argument(
        "--plot", "-p", action="store_true", help="Generate plots of the data"
    )

    parser.add_argument(
        "--statistics",
        choices=["basic", "detailed", "all"],
        default="basic",
        help="Level of statistical analysis (default: basic)",
    )

    parser.add_argument(
        "--format",
        choices=["text", "json", "csv"],
        default="text",
        help="Output format (default: text)",
    )

    parser.add_argument(
        "--threshold",
        type=float,
        default=5.0,
        help="Threshold for high inflammation detection (default: 5.0)",
    )

    return parser


def advanced_inflammation_analyzer(args):
    """Advanced analyzer using argparse."""

    if args.verbose:
        print(f"🔍 Starting analysis with following parameters:")
        print(f"🔍   File: {args.filename}")
        print(f"🔍   Output: {args.output or 'stdout'}")
        print(f"🔍   Statistics level: {args.statistics}")
        print(f"🔍   Format: {args.format}")
        print(f"🔍   Threshold: {args.threshold}")
        print(f"🔍   Generate plots: {args.plot}")

    # Validate input file
    if not os.path.exists(args.filename):
        print(f"Error: File '{args.filename}' not found.")
        return False

    # Simulate data loading and analysis
    if args.verbose:
        print(f"🔍 Loading data from {args.filename}...")

    # Simulated analysis results
    basic_stats = {"mean": 6.14, "max": 18, "min": 0, "patients": 60, "days": 40}

    detailed_stats = {**basic_stats, "std": 4.61, "median": 5.0, "q25": 2.0, "q75": 9.0}

    # High inflammation analysis
    high_inflammation_days = 12  # Simulated
    high_percentage = (high_inflammation_days / basic_stats["days"]) * 100

    # Select statistics based on level
    if args.statistics == "basic":
        stats = basic_stats
    elif args.statistics == "detailed":
        stats = detailed_stats
    else:  # 'all'
        stats = {
            **detailed_stats,
            "high_inflammation_days": high_inflammation_days,
            "high_percentage": high_percentage,
        }

    # Format output
    if args.format == "json":
        import json

        output = json.dumps(stats, indent=2)
    elif args.format == "csv":
        header = ",".join(stats.keys())
        values = ",".join(str(v) for v in stats.values())
        output = f"{header}\n{values}"
    else:  # text format
        output = f"Inflammation Analysis Results\n"
        output += f"{'='*30}\n"
        output += f"File: {args.filename}\n"
        for key, value in stats.items():
            if isinstance(value, float):
                output += f"{key.replace('_', ' ').title()}: {value:.2f}\n"
            else:
                output += f"{key.replace('_', ' ').title()}: {value}\n"

        if args.threshold in stats:
            output += f"\nHigh inflammation (>{args.threshold}):\n"
            output += f"  Days: {stats.get('high_inflammation_days', 'N/A')}\n"
            output += f"  Percentage: {stats.get('high_percentage', 'N/A'):.1f}%\n"

    # Output results
    if args.output:
        if args.verbose:
            print(f"🔍 Writing results to {args.output}")

        try:
            with open(args.output, "w") as f:
                f.write(output)
            print(f"Results written to {args.output}")
        except IOError as e:
            print(f"Error writing to file: {e}")
            return False
    else:
        print(output)

    # Generate plots if requested
    if args.plot:
        if args.verbose:
            print(f"🔍 Generating plots...")

        # Simulate plot generation
        plot_filename = f"{Path(args.filename).stem}_plots.png"
        print(f"📊 Plot would be saved as: {plot_filename}")
        print("📊 (Matplotlib plotting code would go here)")

    return True


# Test advanced analyzer
print("Testing advanced analyzer with argparse:")

# Simulate different command-line scenarios
test_scenarios = [
    ["data/inflammation-01.csv"],
    ["data/inflammation-01.csv", "--verbose"],
    ["data/inflammation-01.csv", "--statistics", "detailed", "--format", "json"],
    ["data/inflammation-01.csv", "--plot", "--output", "results.txt"],
    ["nonexistent.csv"],  # This should fail
]

parser = create_argument_parser()

for i, test_args in enumerate(test_scenarios, 1):
    print(f"\n--- Test {i}: {' '.join(test_args)} ---")

    try:
        args = parser.parse_args(test_args)
        success = advanced_inflammation_analyzer(args)
        print(f"Result: {'Success' if success else 'Failed'}")
    except SystemExit:
        print("Result: Parser error (would show help or error message)")

# ============================================================
# Command-Line Tools with Multiple Operations
# ============================================================

print("\n=== Multi-Operation Command-Line Tool ===")


def create_multi_operation_parser():
    """Create parser for tool with multiple operations."""

    parser = argparse.ArgumentParser(
        description="Multi-purpose inflammation data analysis tool"
    )

    # Create subcommands
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Analyze command
    analyze_parser = subparsers.add_parser("analyze", help="Analyze inflammation data")
    analyze_parser.add_argument("filename", help="Input CSV file")
    analyze_parser.add_argument("--verbose", "-v", action="store_true")

    # Compare command
    compare_parser = subparsers.add_parser(
        "compare", help="Compare multiple inflammation datasets"
    )
    compare_parser.add_argument("files", nargs="+", help="CSV files to compare")
    compare_parser.add_argument("--output", "-o", help="Output file for comparison")

    # Convert command
    convert_parser = subparsers.add_parser(
        "convert", help="Convert data between formats"
    )
    convert_parser.add_argument("input", help="Input file")
    convert_parser.add_argument("output", help="Output file")
    convert_parser.add_argument(
        "--format", choices=["json", "xml", "csv"], required=True
    )

    # Summary command
    summary_parser = subparsers.add_parser(
        "summary", help="Generate summary statistics for multiple files"
    )
    summary_parser.add_argument("directory", help="Directory containing CSV files")
    summary_parser.add_argument(
        "--pattern", default="inflammation-*.csv", help="File pattern to match"
    )

    return parser


def handle_multi_operations(args):
    """Handle different operations based on command."""

    if args.command == "analyze":
        print(f"📊 Analyzing single file: {args.filename}")
        if args.verbose:
            print("🔍 Verbose mode enabled")
        # Analysis code would go here

    elif args.command == "compare":
        print(f"📊 Comparing {len(args.files)} files:")
        for f in args.files:
            print(f"  - {f}")
        if args.output:
            print(f"📝 Results will be saved to: {args.output}")
        # Comparison code would go here

    elif args.command == "convert":
        print(f"🔄 Converting {args.input} to {args.format} format")
        print(f"📝 Output: {args.output}")
        # Conversion code would go here

    elif args.command == "summary":
        print(f"📋 Generating summary for files in: {args.directory}")
        print(f"🔍 Pattern: {args.pattern}")
        # Summary generation code would go here

    else:
        print("❌ No command specified. Use --help for usage information.")
        return False

    return True


# Test multi-operation tool
print("Testing multi-operation tool:")

multi_parser = create_multi_operation_parser()

multi_test_scenarios = [
    ["analyze", "data/inflammation-01.csv", "--verbose"],
    [
        "compare",
        "data/inflammation-01.csv",
        "data/inflammation-02.csv",
        "--output",
        "comparison.txt",
    ],
    ["convert", "data/inflammation-01.csv", "output.json", "--format", "json"],
    ["summary", "data/", "--pattern", "*.csv"],
    [],  # No command - should show error
]

for i, test_args in enumerate(multi_test_scenarios, 1):
    print(f"\n--- Multi-Test {i}: {' '.join(test_args)} ---")

    try:
        args = multi_parser.parse_args(test_args)
        success = handle_multi_operations(args)
        print(f"Result: {'Success' if success else 'Failed'}")
    except SystemExit:
        print("Result: Parser error (would show help or error message)")

# ============================================================
# Unix-Style Pipeline Integration
# ============================================================

print("\n=== Unix-Style Pipeline Integration ===")


def create_pipeline_friendly_tool():
    """Create a tool that works well in Unix pipelines."""

    def process_stdin():
        """Process data from standard input."""
        print("📥 Reading from standard input...")

        # Simulate reading from stdin
        # In real implementation: data = sys.stdin.read()
        simulated_input = "1,2,3,4,5\n6,7,8,9,10\n"

        lines = simulated_input.strip().split("\n")
        total_sum = 0
        line_count = 0

        for line in lines:
            if line.strip():
                values = [int(x) for x in line.split(",")]
                line_sum = sum(values)
                total_sum += line_sum
                line_count += 1
                print(f"Line {line_count}: sum = {line_sum}")

        average = total_sum / line_count if line_count > 0 else 0
        print(f"Overall average: {average:.2f}")

        return average

    def process_file(filename):
        """Process data from a file."""
        print(f"📁 Processing file: {filename}")

        if not os.path.exists(filename):
            print(f"Error: File {filename} not found", file=sys.stderr)
            return None

        # Simulate file processing
        print(f"✓ File processed successfully")
        return 6.14  # Simulated result

    # Determine input source
    if len(sys.argv) > 1 and sys.argv[1] != "-":
        # File input
        filename = sys.argv[1]
        result = process_file(filename)
    else:
        # stdin input (for pipeline usage)
        result = process_stdin()

    # Output result in pipeline-friendly format
    if result is not None:
        print(f"{result:.2f}")  # Just the number for easy parsing

    return result


print("Simulating pipeline-friendly tool:")

# Test with file input
print("1. File input mode:")
sys.argv = ["pipeline_tool.py", "data/inflammation-01.csv"]
create_pipeline_friendly_tool()

print("\n2. Stdin input mode (pipeline):")
sys.argv = ["pipeline_tool.py", "-"]
create_pipeline_friendly_tool()

# ============================================================
# Command-Line Best Practices Summary
# ============================================================

print("\n" + "=" * 60)
print("=== Command-Line Programming Best Practices ===")
print("=" * 60)

best_practices = [
    "📋 ARGUMENT HANDLING:",
    "  • Use argparse for robust command-line parsing",
    "  • Provide clear help messages and examples",
    "  • Validate all inputs before processing",
    "  • Support both file and stdin input for pipeline usage",
    "",
    "📤 OUTPUT DESIGN:",
    "  • Write normal output to stdout, errors to stderr",
    "  • Support multiple output formats (text, JSON, CSV)",
    "  • Make output easily parseable by other tools",
    "  • Use consistent exit codes (0 for success, non-zero for errors)",
    "",
    "🔧 FUNCTIONALITY:",
    "  • Do one thing well (Unix philosophy)",
    "  • Support batch processing of multiple files",
    "  • Provide verbose and quiet modes",
    "  • Include progress indicators for long operations",
    "",
    "🚨 ERROR HANDLING:",
    "  • Check file existence before processing",
    "  • Provide meaningful error messages",
    "  • Handle interruptions gracefully (Ctrl+C)",
    "  • Clean up temporary files on exit",
    "",
    "📖 DOCUMENTATION:",
    "  • Include comprehensive help text",
    "  • Provide usage examples",
    "  • Document expected input formats",
    "  • Explain output format and meaning",
]

for practice in best_practices:
    print(practice)

print("\n💡 Example pipeline usage:")
print("  cat data/*.csv | python analyzer.py - | sort -n | tail -5")
print("  python analyzer.py data/inflammation-01.csv --format json | jq '.mean'")
print("  find data/ -name '*.csv' | xargs python analyzer.py --summary")

print("\n🎯 Remember: Good command-line tools are composable and predictable!")
