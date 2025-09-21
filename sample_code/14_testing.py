# Episode 14: Testing in Python
# Sample code demonstrating testing practices for scientific Python code

import sys
import os
import unittest
from unittest.mock import Mock, patch, MagicMock
import tempfile
import csv
from typing import List, Dict, Optional, Tuple
from pathlib import Path

# Add current directory to path for importing our modules
sys.path.insert(0, os.path.dirname(__file__))

# ============================================================
# Code Under Test - Inflammation Analysis Functions
# ============================================================


class InflammationAnalyzer:
    """Class for analyzing inflammation data - our code under test."""

    def __init__(self, data_directory: str = "data"):
        self.data_directory = data_directory
        self.cache: Dict[str, List[List[float]]] = {}

    def load_inflammation_data(self, filename: str) -> List[List[float]]:
        """Load inflammation data from CSV file."""
        if filename in self.cache:
            return self.cache[filename]

        filepath = os.path.join(self.data_directory, filename)
        data = []

        try:
            with open(filepath, "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    # Convert string values to floats
                    numeric_row = [float(value) for value in row if value.strip()]
                    if numeric_row:  # Only add non-empty rows
                        data.append(numeric_row)
        except FileNotFoundError:
            raise FileNotFoundError(f"Data file not found: {filepath}")
        except ValueError as e:
            raise ValueError(f"Invalid data format in {filename}: {e}")

        # Cache the result
        self.cache[filename] = data
        return data

    def calculate_daily_averages(self, data: List[List[float]]) -> List[float]:
        """Calculate average inflammation for each day."""
        if not data:
            return []

        num_days = len(data[0])
        daily_sums = [0.0] * num_days

        for patient_data in data:
            for day, inflammation in enumerate(patient_data):
                daily_sums[day] += inflammation

        num_patients = len(data)
        return [daily_sum / num_patients for daily_sum in daily_sums]

    def find_max_inflammation_patient(
        self, data: List[List[float]]
    ) -> Tuple[int, float]:
        """Find patient with highest total inflammation."""
        if not data:
            return (-1, 0.0)

        max_total = 0.0
        max_patient_index = 0

        for i, patient_data in enumerate(data):
            total_inflammation = sum(patient_data)
            if total_inflammation > max_total:
                max_total = total_inflammation
                max_patient_index = i

        return (max_patient_index, max_total)

    def detect_anomalies(
        self, data: List[List[float]], threshold: float = 0.0
    ) -> List[Tuple[int, int]]:
        """Detect anomalous inflammation readings (exactly 0.0 or above threshold)."""
        anomalies = []

        for patient_idx, patient_data in enumerate(data):
            for day_idx, inflammation in enumerate(patient_data):
                if inflammation == 0.0 or (threshold > 0 and inflammation > threshold):
                    anomalies.append((patient_idx, day_idx))

        return anomalies

    def generate_summary_report(self, filename: str) -> Dict[str, any]:
        """Generate a comprehensive summary report."""
        try:
            data = self.load_inflammation_data(filename)

            daily_averages = self.calculate_daily_averages(data)
            max_patient_idx, max_inflammation = self.find_max_inflammation_patient(data)
            anomalies = self.detect_anomalies(data, threshold=20.0)

            return {
                "filename": filename,
                "num_patients": len(data),
                "num_days": len(data[0]) if data else 0,
                "overall_average": (
                    sum(daily_averages) / len(daily_averages) if daily_averages else 0.0
                ),
                "max_patient_index": max_patient_idx,
                "max_total_inflammation": max_inflammation,
                "num_anomalies": len(anomalies),
                "anomaly_rate": (
                    len(anomalies) / (len(data) * len(data[0])) if data else 0.0
                ),
            }

        except Exception as e:
            return {"error": str(e), "filename": filename}


# ============================================================
# Unit Tests with unittest
# ============================================================

print("=== Unit Testing with unittest ===")


class TestInflammationAnalyzer(unittest.TestCase):
    """Test cases for InflammationAnalyzer class."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        # Create a temporary directory for test data
        self.test_dir = tempfile.mkdtemp()
        self.analyzer = InflammationAnalyzer(data_directory=self.test_dir)

        # Create sample test data
        self.sample_data = [
            [0.0, 1.0, 2.0, 3.0, 2.0, 1.0, 0.0],  # Patient 0
            [1.0, 2.0, 3.0, 4.0, 3.0, 2.0, 1.0],  # Patient 1
            [0.0, 0.5, 1.0, 1.5, 1.0, 0.5, 0.0],  # Patient 2
        ]

        # Create a test CSV file
        self.test_filename = "test_inflammation.csv"
        self.test_filepath = os.path.join(self.test_dir, self.test_filename)

        with open(self.test_filepath, "w", newline="") as file:
            writer = csv.writer(file)
            for row in self.sample_data:
                writer.writerow(row)

    def tearDown(self):
        """Clean up after each test method."""
        # Remove test files
        import shutil

        shutil.rmtree(self.test_dir, ignore_errors=True)

    def test_load_inflammation_data_success(self):
        """Test successful loading of inflammation data."""
        data = self.analyzer.load_inflammation_data(self.test_filename)

        self.assertEqual(len(data), 3)  # 3 patients
        self.assertEqual(len(data[0]), 7)  # 7 days
        self.assertEqual(data[0][0], 0.0)  # First reading
        self.assertEqual(data[1][3], 4.0)  # Patient 1, day 3

    def test_load_inflammation_data_file_not_found(self):
        """Test error handling for missing file."""
        with self.assertRaises(FileNotFoundError):
            self.analyzer.load_inflammation_data("nonexistent.csv")

    def test_load_inflammation_data_caching(self):
        """Test that data is properly cached."""
        # Load data twice
        data1 = self.analyzer.load_inflammation_data(self.test_filename)
        data2 = self.analyzer.load_inflammation_data(self.test_filename)

        # Should be the same object (cached)
        self.assertIs(data1, data2)
        self.assertIn(self.test_filename, self.analyzer.cache)

    def test_calculate_daily_averages(self):
        """Test daily average calculation."""
        averages = self.analyzer.calculate_daily_averages(self.sample_data)

        expected_averages = [
            (0.0 + 1.0 + 0.0) / 3,  # Day 0: 0.333...
            (1.0 + 2.0 + 0.5) / 3,  # Day 1: 1.166...
            (2.0 + 3.0 + 1.0) / 3,  # Day 2: 2.0
            (3.0 + 4.0 + 1.5) / 3,  # Day 3: 2.833...
            (2.0 + 3.0 + 1.0) / 3,  # Day 4: 2.0
            (1.0 + 2.0 + 0.5) / 3,  # Day 5: 1.166...
            (0.0 + 1.0 + 0.0) / 3,  # Day 6: 0.333...
        ]

        self.assertEqual(len(averages), 7)
        for i, expected in enumerate(expected_averages):
            self.assertAlmostEqual(averages[i], expected, places=2)

    def test_calculate_daily_averages_empty_data(self):
        """Test daily averages with empty data."""
        averages = self.analyzer.calculate_daily_averages([])
        self.assertEqual(averages, [])

    def test_find_max_inflammation_patient(self):
        """Test finding patient with maximum inflammation."""
        patient_idx, max_inflammation = self.analyzer.find_max_inflammation_patient(
            self.sample_data
        )

        # Patient 1 has total: 1+2+3+4+3+2+1 = 16
        # Patient 0 has total: 0+1+2+3+2+1+0 = 9
        # Patient 2 has total: 0+0.5+1+1.5+1+0.5+0 = 4.5
        self.assertEqual(patient_idx, 1)
        self.assertAlmostEqual(max_inflammation, 16.0)

    def test_find_max_inflammation_patient_empty_data(self):
        """Test max inflammation with empty data."""
        patient_idx, max_inflammation = self.analyzer.find_max_inflammation_patient([])
        self.assertEqual(patient_idx, -1)
        self.assertEqual(max_inflammation, 0.0)

    def test_detect_anomalies(self):
        """Test anomaly detection."""
        # Test detecting zero values
        anomalies = self.analyzer.detect_anomalies(self.sample_data, threshold=0.0)

        # Should find zero values at (0,0), (0,6), (2,0), (2,6)
        zero_anomalies = [
            (patient, day)
            for patient, day in anomalies
            if self.sample_data[patient][day] == 0.0
        ]
        self.assertEqual(len(zero_anomalies), 4)
        self.assertIn((0, 0), zero_anomalies)
        self.assertIn((0, 6), zero_anomalies)
        self.assertIn((2, 0), zero_anomalies)
        self.assertIn((2, 6), zero_anomalies)

    def test_detect_anomalies_with_threshold(self):
        """Test anomaly detection with threshold."""
        # Test with threshold of 3.5 (should catch 4.0 reading)
        anomalies = self.analyzer.detect_anomalies(self.sample_data, threshold=3.5)

        # Should find value 4.0 at (1, 3) plus all zeros
        high_value_anomalies = [
            (patient, day)
            for patient, day in anomalies
            if self.sample_data[patient][day] > 3.5
        ]
        self.assertEqual(len(high_value_anomalies), 1)
        self.assertIn((1, 3), high_value_anomalies)

    def test_generate_summary_report(self):
        """Test summary report generation."""
        report = self.analyzer.generate_summary_report(self.test_filename)

        self.assertEqual(report["filename"], self.test_filename)
        self.assertEqual(report["num_patients"], 3)
        self.assertEqual(report["num_days"], 7)
        self.assertEqual(report["max_patient_index"], 1)
        self.assertAlmostEqual(report["max_total_inflammation"], 16.0)
        self.assertIn("num_anomalies", report)
        self.assertIn("anomaly_rate", report)

    def test_generate_summary_report_error_handling(self):
        """Test summary report error handling."""
        report = self.analyzer.generate_summary_report("nonexistent.csv")

        self.assertIn("error", report)
        self.assertEqual(report["filename"], "nonexistent.csv")


# ============================================================
# Advanced Testing Techniques
# ============================================================

print("\n=== Advanced Testing with Mocks and Patches ===")


class TestInflammationAnalyzerAdvanced(unittest.TestCase):
    """Advanced test cases using mocks and patches."""

    def setUp(self):
        self.analyzer = InflammationAnalyzer("fake_directory")

    @patch("builtins.open")
    def test_load_data_with_mock_file(self, mock_open):
        """Test data loading with mocked file operations."""
        # Mock CSV data
        mock_csv_content = "0.0,1.0,2.0\n1.0,2.0,3.0\n"
        mock_open.return_value.__enter__.return_value = mock_csv_content.splitlines()

        # This test is more complex and requires additional mocking
        # In practice, you'd use pytest with better mocking capabilities
        pass

    def test_calculate_averages_with_mock_data(self):
        """Test calculations with controlled test data."""
        # Create predictable test data
        mock_data = [[1.0, 2.0, 3.0], [2.0, 4.0, 6.0], [3.0, 6.0, 9.0]]

        averages = self.analyzer.calculate_daily_averages(mock_data)
        expected = [2.0, 4.0, 6.0]  # (1+2+3)/3, (2+4+6)/3, (3+6+9)/3

        for i, expected_avg in enumerate(expected):
            self.assertAlmostEqual(averages[i], expected_avg)

    @patch.object(InflammationAnalyzer, "load_inflammation_data")
    def test_summary_report_with_mocked_loader(self, mock_loader):
        """Test summary report with mocked data loader."""
        # Set up mock return value
        mock_data = [[1.0, 2.0, 3.0, 2.0, 1.0], [2.0, 3.0, 4.0, 3.0, 2.0]]
        mock_loader.return_value = mock_data

        report = self.analyzer.generate_summary_report("test.csv")

        # Verify mock was called
        mock_loader.assert_called_once_with("test.csv")

        # Verify report contents
        self.assertEqual(report["num_patients"], 2)
        self.assertEqual(report["num_days"], 5)


# ============================================================
# Property-Based Testing Example
# ============================================================

print("\n=== Property-Based Testing Concepts ===")


class TestInflammationProperties(unittest.TestCase):
    """Property-based testing examples."""

    def setUp(self):
        self.analyzer = InflammationAnalyzer()

    def test_daily_averages_properties(self):
        """Test mathematical properties of daily averages."""
        # Property: Number of averages should equal number of days
        test_data = [[1.0, 2.0, 3.0, 4.0], [2.0, 3.0, 4.0, 5.0], [3.0, 4.0, 5.0, 6.0]]

        averages = self.analyzer.calculate_daily_averages(test_data)
        self.assertEqual(len(averages), 4)  # Should have 4 daily averages

        # Property: All averages should be >= minimum individual reading
        min_reading = min(min(patient) for patient in test_data)
        for avg in averages:
            self.assertGreaterEqual(avg, min_reading)

        # Property: All averages should be <= maximum individual reading
        max_reading = max(max(patient) for patient in test_data)
        for avg in averages:
            self.assertLessEqual(avg, max_reading)

    def test_anomaly_detection_properties(self):
        """Test properties of anomaly detection."""
        test_data = [
            [0.0, 1.0, 0.0, 25.0],  # Has zero and high value
            [2.0, 3.0, 4.0, 5.0],  # Normal values
        ]

        anomalies = self.analyzer.detect_anomalies(test_data, threshold=20.0)

        # Property: All detected anomalies should be either 0.0 or > threshold
        for patient_idx, day_idx in anomalies:
            value = test_data[patient_idx][day_idx]
            self.assertTrue(value == 0.0 or value > 20.0)

        # Property: Number of anomalies should be <= total readings
        total_readings = sum(len(patient) for patient in test_data)
        self.assertLessEqual(len(anomalies), total_readings)


# ============================================================
# Test Fixtures and Test Data Management
# ============================================================

print("\n=== Test Fixtures and Data Management ===")


class InflammationTestData:
    """Test data factory for inflammation testing."""

    @staticmethod
    def create_normal_data(
        num_patients: int = 3, num_days: int = 5
    ) -> List[List[float]]:
        """Create normal inflammation data for testing."""
        import random

        random.seed(42)  # Ensure reproducible tests

        data = []
        for patient in range(num_patients):
            patient_data = []
            for day in range(num_days):
                # Generate realistic inflammation pattern (starts low, peaks, then decreases)
                base_inflammation = 2.0 + random.uniform(-0.5, 0.5)
                day_factor = (
                    1.0 + (day / num_days) * 2.0
                    if day < num_days // 2
                    else 3.0 - (day / num_days) * 2.0
                )
                inflammation = base_inflammation * day_factor
                patient_data.append(round(inflammation, 1))
            data.append(patient_data)

        return data

    @staticmethod
    def create_anomalous_data() -> List[List[float]]:
        """Create data with known anomalies for testing."""
        return [
            [0.0, 1.0, 2.0, 0.0, 1.0],  # Patient with zero inflammation
            [5.0, 6.0, 25.0, 4.0, 3.0],  # Patient with spike
            [1.0, 1.5, 2.0, 1.5, 1.0],  # Normal patient
        ]

    @staticmethod
    def create_edge_case_data() -> Dict[str, List[List[float]]]:
        """Create various edge case datasets."""
        return {
            "empty": [],
            "single_patient": [[1.0, 2.0, 3.0]],
            "single_day": [[1.0], [2.0], [3.0]],
            "all_zeros": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]],
            "large_values": [[100.0, 200.0, 300.0], [150.0, 250.0, 350.0]],
        }


class TestWithFixtures(unittest.TestCase):
    """Test class demonstrating fixture usage."""

    @classmethod
    def setUpClass(cls):
        """Set up class-level fixtures (run once for all tests)."""
        cls.test_data_factory = InflammationTestData()
        cls.analyzer = InflammationAnalyzer()

    def test_normal_data_processing(self):
        """Test with normal inflammation data."""
        data = self.test_data_factory.create_normal_data(5, 7)

        averages = self.analyzer.calculate_daily_averages(data)
        self.assertEqual(len(averages), 7)

        # All averages should be positive for normal data
        for avg in averages:
            self.assertGreater(avg, 0)

    def test_anomalous_data_detection(self):
        """Test anomaly detection with known anomalous data."""
        data = self.test_data_factory.create_anomalous_data()

        anomalies = self.analyzer.detect_anomalies(data, threshold=20.0)

        # Should detect zeros and the spike value (25.0)
        self.assertGreater(len(anomalies), 0)

        # Verify specific anomalies are detected
        anomaly_positions = set(anomalies)
        self.assertIn((0, 0), anomaly_positions)  # Zero at (0,0)
        self.assertIn((0, 3), anomaly_positions)  # Zero at (0,3)
        self.assertIn((1, 2), anomaly_positions)  # Spike at (1,2)

    def test_edge_cases(self):
        """Test various edge cases."""
        edge_cases = self.test_data_factory.create_edge_case_data()

        # Test empty data
        averages = self.analyzer.calculate_daily_averages(edge_cases["empty"])
        self.assertEqual(averages, [])

        # Test single patient
        averages = self.analyzer.calculate_daily_averages(edge_cases["single_patient"])
        self.assertEqual(averages, [1.0, 2.0, 3.0])

        # Test all zeros
        anomalies = self.analyzer.detect_anomalies(edge_cases["all_zeros"])
        self.assertEqual(len(anomalies), 6)  # All 6 readings should be anomalies


# ============================================================
# Performance Testing
# ============================================================

print("\n=== Performance Testing ===")


class TestPerformance(unittest.TestCase):
    """Performance testing examples."""

    def setUp(self):
        self.analyzer = InflammationAnalyzer()

    def test_large_dataset_performance(self):
        """Test performance with large datasets."""
        import time

        # Create large dataset
        large_data = InflammationTestData.create_normal_data(
            1000, 365
        )  # 1000 patients, 365 days

        # Time the calculation
        start_time = time.time()
        averages = self.analyzer.calculate_daily_averages(large_data)
        end_time = time.time()

        execution_time = end_time - start_time

        # Performance assertion (should complete in reasonable time)
        self.assertLess(execution_time, 1.0)  # Should complete in less than 1 second
        self.assertEqual(len(averages), 365)

        print(f"  Large dataset processing time: {execution_time:.3f} seconds")

    def test_memory_usage_pattern(self):
        """Test memory usage patterns."""
        # Test that caching works efficiently
        import sys

        self.analyzer.cache.clear()
        initial_cache_size = len(self.analyzer.cache)

        # Create test data
        test_data = InflammationTestData.create_normal_data(10, 10)

        # Simulate file loading (we'll just cache directly for this test)
        self.analyzer.cache["test1.csv"] = test_data
        self.analyzer.cache["test2.csv"] = test_data

        # Verify cache growth
        self.assertEqual(len(self.analyzer.cache), initial_cache_size + 2)


# ============================================================
# Integration Testing
# ============================================================

print("\n=== Integration Testing ===")


class TestIntegration(unittest.TestCase):
    """Integration tests that test multiple components together."""

    def setUp(self):
        # Create temporary test environment
        self.test_dir = tempfile.mkdtemp()
        self.analyzer = InflammationAnalyzer(data_directory=self.test_dir)

        # Create multiple test files
        self.test_files = ["inflammation-01.csv", "inflammation-02.csv"]

        for i, filename in enumerate(self.test_files):
            filepath = os.path.join(self.test_dir, filename)
            test_data = InflammationTestData.create_normal_data(5 + i, 10)

            with open(filepath, "w", newline="") as file:
                writer = csv.writer(file)
                for row in test_data:
                    writer.writerow(row)

    def tearDown(self):
        import shutil

        shutil.rmtree(self.test_dir, ignore_errors=True)

    def test_complete_analysis_workflow(self):
        """Test complete analysis workflow from file to report."""
        reports = []

        for filename in self.test_files:
            report = self.analyzer.generate_summary_report(filename)
            self.assertNotIn("error", report)
            reports.append(report)

        # Verify all reports were generated successfully
        self.assertEqual(len(reports), 2)

        # Verify caching worked
        self.assertEqual(len(self.analyzer.cache), 2)

        # Verify reports have expected structure
        for report in reports:
            required_keys = [
                "filename",
                "num_patients",
                "num_days",
                "overall_average",
                "max_patient_index",
                "max_total_inflammation",
                "num_anomalies",
            ]
            for key in required_keys:
                self.assertIn(key, report)

    def test_cross_file_comparison(self):
        """Test comparing results across multiple files."""
        report1 = self.analyzer.generate_summary_report(self.test_files[0])
        report2 = self.analyzer.generate_summary_report(self.test_files[1])

        # Both should be successful
        self.assertNotIn("error", report1)
        self.assertNotIn("error", report2)

        # Different files should have different patient counts (5 vs 6)
        self.assertNotEqual(report1["num_patients"], report2["num_patients"])

        # Both should have same number of days (10)
        self.assertEqual(report1["num_days"], report2["num_days"])


# ============================================================
# Test Discovery and Running
# ============================================================


def run_all_tests():
    """Run all test suites."""
    print("=== Running All Tests ===")

    # Create test suite
    test_suite = unittest.TestSuite()

    # Add test classes
    test_classes = [
        TestInflammationAnalyzer,
        TestInflammationAnalyzerAdvanced,
        TestInflammationProperties,
        TestWithFixtures,
        TestPerformance,
        TestIntegration,
    ]

    for test_class in test_classes:
        tests = unittest.TestLoader().loadTestsFromTestCase(test_class)
        test_suite.addTests(tests)

    # Run tests with detailed output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)

    # Print summary
    print(f"\n=== Test Summary ===")
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(
        f"Success rate: {((result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100):.1f}%"
    )

    return result.wasSuccessful()


# ============================================================
# Testing Best Practices and Tips
# ============================================================


def demonstrate_testing_principles():
    """Demonstrate testing best practices."""
    print("\n=== Testing Best Practices ===")

    best_practices = [
        "✓ Test one thing at a time (single responsibility)",
        "✓ Use descriptive test names that explain what is being tested",
        "✓ Follow AAA pattern: Arrange, Act, Assert",
        "✓ Use setUp/tearDown for test fixtures",
        "✓ Test both positive and negative cases",
        "✓ Test edge cases and boundary conditions",
        "✓ Use mocks to isolate units under test",
        "✓ Keep tests independent - no test should depend on another",
        "✓ Make tests fast and deterministic",
        "✓ Aim for high test coverage but focus on critical paths",
        "✓ Use property-based testing for mathematical functions",
        "✓ Include performance and integration tests",
        "✓ Keep test data separate from production data",
        "✓ Use factories for creating test data",
        "✓ Write tests before or alongside code (TDD/BDD)",
    ]

    for practice in best_practices:
        print(f"  {practice}")

    print("\n=== Test Organization Tips ===")
    organization_tips = [
        "📁 tests/unit/ - Unit tests for individual functions/classes",
        "📁 tests/integration/ - Integration tests for component interaction",
        "📁 tests/performance/ - Performance and load tests",
        "📁 tests/fixtures/ - Test data and utilities",
        "📄 conftest.py - Shared pytest fixtures and configuration",
        "📄 test_requirements.txt - Testing dependencies",
        "🏗️ Use CI/CD to run tests automatically",
        "📊 Generate coverage reports regularly",
        "🏷️ Tag tests by type (unit, integration, slow, etc.)",
    ]

    for tip in organization_tips:
        print(f"  {tip}")


# ============================================================
# Main Execution
# ============================================================

if __name__ == "__main__":
    print("🧪 Python Testing Comprehensive Guide")
    print("=====================================")

    # Demonstrate testing principles
    demonstrate_testing_principles()

    # Run example tests
    print("\n" + "=" * 50)
    print("Running Example Tests...")

    try:
        success = run_all_tests()
        if success:
            print("\n🎉 All tests passed!")
        else:
            print("\n❌ Some tests failed. Check output above.")
    except Exception as e:
        print(f"\n⚠️ Error running tests: {e}")

    print("\n=== Alternative Testing Frameworks ===")
    print("🔧 pytest: pip install pytest")
    print("   - More powerful fixtures and parameterization")
    print("   - Better output and debugging")
    print("   - Extensive plugin ecosystem")
    print("   - Run with: pytest test_file.py")
    print()
    print("🔧 nose2: pip install nose2")
    print("   - Extended unittest runner")
    print("   - Plugin architecture")
    print("   - Run with: nose2")
    print()
    print("🔧 doctest: Built-in Python module")
    print("   - Tests embedded in docstrings")
    print("   - Great for documentation examples")
    print("   - Run with: python -m doctest module.py")
    print()
    print("🔧 hypothesis: pip install hypothesis")
    print("   - Property-based testing")
    print("   - Automatic test case generation")
    print("   - Great for finding edge cases")

    print(
        "\n💡 Testing improves code quality, catches bugs early, and enables confident refactoring!"
    )
    print(
        "💡 Start with simple unit tests and gradually add integration and performance tests."
    )
