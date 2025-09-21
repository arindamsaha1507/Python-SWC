# Episode 13: Type Hinting in Python
# Sample code demonstrating type hints for better code documentation and IDE support

from typing import List, Dict, Tuple, Optional, Union, Any, Callable
from typing import TypeVar, Generic
import sys

# ============================================================
# Basic Type Hints
# ============================================================

print("=== Basic Type Hints ===")


def calculate_inflammation_average(readings: List[float]) -> float:
    """
    Calculate average inflammation with type hints.

    Args:
        readings: List of inflammation readings as floats

    Returns:
        Average inflammation as float
    """
    if not readings:
        return 0.0

    total: float = sum(readings)
    count: int = len(readings)
    average: float = total / count

    return average


# Variables with type hints
patient_name: str = "Alice Smith"
patient_age: int = 45
inflammation_level: float = 6.2
has_chronic_condition: bool = True

print(f"Patient: {patient_name}")
print(f"Age: {patient_age}")
print(f"Inflammation level: {inflammation_level}")
print(f"Has chronic condition: {has_chronic_condition}")

# Test the function
sample_readings: List[float] = [2.1, 3.5, 1.8, 4.2, 5.1]
avg_inflammation: float = calculate_inflammation_average(sample_readings)
print(f"Average inflammation: {avg_inflammation:.2f}")

# ============================================================
# Collection Types
# ============================================================

print("\n=== Collection Types ===")


def analyze_patient_data(patient_records: Dict[str, List[float]]) -> Dict[str, float]:
    """
    Analyze multiple patients' inflammation data.

    Args:
        patient_records: Dictionary mapping patient IDs to their daily readings

    Returns:
        Dictionary mapping patient IDs to their average inflammation
    """
    results: Dict[str, float] = {}

    for patient_id, readings in patient_records.items():
        if readings:  # Check if readings exist
            avg: float = sum(readings) / len(readings)
            results[patient_id] = avg
        else:
            results[patient_id] = 0.0

    return results


# Sample data with type hints
patients_data: Dict[str, List[float]] = {
    "P001": [2.1, 3.2, 1.5, 4.1, 2.8],
    "P002": [1.8, 2.7, 3.1, 2.4, 1.9],
    "P003": [4.2, 5.1, 3.8, 4.7, 4.0],
}

analysis_results: Dict[str, float] = analyze_patient_data(patients_data)
print("Patient analysis results:")
for patient_id, avg in analysis_results.items():
    print(f"  {patient_id}: {avg:.2f}")

# ============================================================
# Tuple Types and Named Tuples
# ============================================================

print("\n=== Tuple Types ===")


def get_inflammation_stats(readings: List[float]) -> Tuple[float, float, float]:
    """
    Get inflammation statistics: (mean, min, max).

    Args:
        readings: List of inflammation readings

    Returns:
        Tuple of (mean, minimum, maximum) values
    """
    if not readings:
        return (0.0, 0.0, 0.0)

    mean_val: float = sum(readings) / len(readings)
    min_val: float = min(readings)
    max_val: float = max(readings)

    return (mean_val, min_val, max_val)


# Using tuple unpacking with type hints
sample_data: List[float] = [1.2, 3.4, 2.1, 5.6, 2.8, 4.1]
mean, minimum, maximum = get_inflammation_stats(sample_data)

print(f"Statistics: mean={mean:.2f}, min={minimum:.2f}, max={maximum:.2f}")

# Named tuples for better structure
from typing import NamedTuple


class InflammationStats(NamedTuple):
    """Named tuple for inflammation statistics."""

    mean: float
    minimum: float
    maximum: float
    count: int


def get_detailed_stats(readings: List[float]) -> InflammationStats:
    """Get detailed inflammation statistics."""
    if not readings:
        return InflammationStats(0.0, 0.0, 0.0, 0)

    mean_val = sum(readings) / len(readings)
    min_val = min(readings)
    max_val = max(readings)
    count = len(readings)

    return InflammationStats(mean_val, min_val, max_val, count)


detailed_stats: InflammationStats = get_detailed_stats(sample_data)
print(f"Detailed stats: {detailed_stats}")
print(f"Mean: {detailed_stats.mean:.2f}")

# ============================================================
# Optional and Union Types
# ============================================================

print("\n=== Optional and Union Types ===")


def find_patient_by_id(
    patient_id: str, database: Dict[str, Dict[str, Any]]
) -> Optional[Dict[str, Any]]:
    """
    Find patient by ID, return None if not found.

    Args:
        patient_id: Patient identifier
        database: Patient database

    Returns:
        Patient data dictionary or None if not found
    """
    return database.get(patient_id)


def process_inflammation_reading(value: Union[str, int, float]) -> float:
    """
    Process inflammation reading that might be string or number.

    Args:
        value: Reading value as string, int, or float

    Returns:
        Processed value as float
    """
    if isinstance(value, str):
        try:
            return float(value.strip())
        except ValueError:
            return 0.0
    elif isinstance(value, (int, float)):
        return float(value)
    else:
        return 0.0


# Sample database
patient_db: Dict[str, Dict[str, Any]] = {
    "P001": {"name": "Alice", "age": 45, "readings": [2.1, 3.2, 1.5]},
    "P002": {"name": "Bob", "age": 52, "readings": [1.8, 2.7, 3.1]},
}

# Test optional return
found_patient: Optional[Dict[str, Any]] = find_patient_by_id("P001", patient_db)
if found_patient is not None:
    print(f"Found patient: {found_patient['name']}")
else:
    print("Patient not found")

missing_patient: Optional[Dict[str, Any]] = find_patient_by_id("P999", patient_db)
if missing_patient is None:
    print("Patient P999 not found")

# Test union types
test_values: List[Union[str, int, float]] = ["3.14", 5, 2.7, "invalid", "  1.5  "]
processed_values: List[float] = [
    process_inflammation_reading(val) for val in test_values
]
print(f"Processed values: {processed_values}")

# ============================================================
# Function Types and Callbacks
# ============================================================

print("\n=== Function Types ===")


def apply_transformation(
    data: List[float], transform_func: Callable[[float], float]
) -> List[float]:
    """
    Apply a transformation function to all data points.

    Args:
        data: List of values to transform
        transform_func: Function that takes float and returns float

    Returns:
        List of transformed values
    """
    return [transform_func(value) for value in data]


def normalize_inflammation(value: float) -> float:
    """Normalize inflammation value to 0-1 scale."""
    # Assuming max normal inflammation is 20
    return min(value / 20.0, 1.0)


def categorize_inflammation(value: float) -> float:
    """Categorize inflammation: 0=none, 1=mild, 2=moderate, 3=severe."""
    if value == 0:
        return 0.0
    elif value <= 2:
        return 1.0
    elif value <= 5:
        return 2.0
    else:
        return 3.0


# Test function types
sample_readings: List[float] = [0, 1.5, 3.2, 7.8, 12.1, 0.5]

normalized: List[float] = apply_transformation(sample_readings, normalize_inflammation)
categorized: List[float] = apply_transformation(
    sample_readings, categorize_inflammation
)

print(f"Original: {sample_readings}")
print(f"Normalized: {[f'{x:.2f}' for x in normalized]}")
print(f"Categorized: {categorized}")

# Lambda functions with type hints
squared: List[float] = apply_transformation(sample_readings, lambda x: x**2)
print(f"Squared: {[f'{x:.1f}' for x in squared]}")

# ============================================================
# Generic Types
# ============================================================

print("\n=== Generic Types ===")

T = TypeVar("T")  # Type variable


class DataProcessor(Generic[T]):
    """Generic data processor that can work with any type."""

    def __init__(self, initial_data: List[T]) -> None:
        self.data: List[T] = initial_data.copy()

    def add_item(self, item: T) -> None:
        """Add an item to the processor."""
        self.data.append(item)

    def get_data(self) -> List[T]:
        """Get all data items."""
        return self.data.copy()

    def filter_data(self, predicate: Callable[[T], bool]) -> List[T]:
        """Filter data based on predicate function."""
        return [item for item in self.data if predicate(item)]


# Use with float data
float_processor: DataProcessor[float] = DataProcessor([1.1, 2.2, 3.3])
float_processor.add_item(4.4)
float_data: List[float] = float_processor.get_data()
print(f"Float processor data: {float_data}")

# Use with string data
string_processor: DataProcessor[str] = DataProcessor(["Patient_001", "Patient_002"])
string_processor.add_item("Patient_003")
string_data: List[str] = string_processor.get_data()
print(f"String processor data: {string_data}")

# Filter with type hints
high_readings: List[float] = float_processor.filter_data(lambda x: x > 3.0)
print(f"High readings: {high_readings}")

# ============================================================
# Class Type Hints
# ============================================================

print("\n=== Class Type Hints ===")


class Patient:
    """Patient class with comprehensive type hints."""

    def __init__(self, patient_id: str, name: str, age: int) -> None:
        self.patient_id: str = patient_id
        self.name: str = name
        self.age: int = age
        self.inflammation_readings: List[float] = []
        self.metadata: Dict[str, Any] = {}

    def add_reading(self, reading: float) -> None:
        """Add an inflammation reading."""
        self.inflammation_readings.append(reading)

    def get_average_inflammation(self) -> Optional[float]:
        """Get average inflammation, None if no readings."""
        if not self.inflammation_readings:
            return None
        return sum(self.inflammation_readings) / len(self.inflammation_readings)

    def get_risk_level(self) -> str:
        """Determine risk level based on age and inflammation."""
        avg_inflammation: Optional[float] = self.get_average_inflammation()

        if avg_inflammation is None:
            return "unknown"

        if self.age >= 65 and avg_inflammation > 5:
            return "high"
        elif avg_inflammation > 7:
            return "high"
        elif avg_inflammation > 3:
            return "medium"
        else:
            return "low"

    def __str__(self) -> str:
        """String representation of patient."""
        avg: Optional[float] = self.get_average_inflammation()
        avg_str: str = f"{avg:.2f}" if avg is not None else "N/A"
        return f"Patient({self.patient_id}, {self.name}, avg_inflammation={avg_str})"


class PatientDatabase:
    """Database of patients with type hints."""

    def __init__(self) -> None:
        self.patients: Dict[str, Patient] = {}

    def add_patient(self, patient: Patient) -> None:
        """Add a patient to the database."""
        self.patients[patient.patient_id] = patient

    def get_patient(self, patient_id: str) -> Optional[Patient]:
        """Get patient by ID."""
        return self.patients.get(patient_id)

    def get_all_patients(self) -> List[Patient]:
        """Get all patients."""
        return list(self.patients.values())

    def find_high_risk_patients(self) -> List[Patient]:
        """Find all high-risk patients."""
        return [p for p in self.patients.values() if p.get_risk_level() == "high"]


# Test the classes
db: PatientDatabase = PatientDatabase()

# Create patients
patient1: Patient = Patient("P001", "Alice Johnson", 67)
patient1.add_reading(2.1)
patient1.add_reading(6.8)
patient1.add_reading(4.3)

patient2: Patient = Patient("P002", "Bob Smith", 34)
patient2.add_reading(1.2)
patient2.add_reading(2.1)
patient2.add_reading(8.5)

# Add to database
db.add_patient(patient1)
db.add_patient(patient2)

# Query database
all_patients: List[Patient] = db.get_all_patients()
high_risk: List[Patient] = db.find_high_risk_patients()

print("All patients:")
for patient in all_patients:
    print(f"  {patient} - Risk: {patient.get_risk_level()}")

print(f"\nHigh-risk patients: {len(high_risk)}")
for patient in high_risk:
    print(f"  {patient}")

# ============================================================
# Type Checking and Runtime Validation
# ============================================================

print("\n=== Type Checking and Validation ===")


def validate_patient_data(data: Dict[str, Any]) -> bool:
    """
    Validate patient data structure at runtime.

    Args:
        data: Dictionary containing patient data

    Returns:
        True if data is valid, False otherwise
    """
    required_fields: List[str] = ["patient_id", "name", "age"]

    # Check required fields
    for field in required_fields:
        if field not in data:
            print(f"Missing required field: {field}")
            return False

    # Check types
    if not isinstance(data["patient_id"], str):
        print("patient_id must be string")
        return False

    if not isinstance(data["name"], str):
        print("name must be string")
        return False

    if not isinstance(data["age"], int):
        print("age must be integer")
        return False

    # Check value ranges
    if data["age"] < 0 or data["age"] > 150:
        print("age must be between 0 and 150")
        return False

    # Check optional readings field
    if "readings" in data:
        if not isinstance(data["readings"], list):
            print("readings must be a list")
            return False

        for i, reading in enumerate(data["readings"]):
            if not isinstance(reading, (int, float)):
                print(f"reading[{i}] must be a number")
                return False

    return True


# Test validation
valid_data: Dict[str, Any] = {
    "patient_id": "P003",
    "name": "Carol Wilson",
    "age": 42,
    "readings": [2.1, 3.4, 1.8],
}

invalid_data: Dict[str, Any] = {
    "patient_id": "P004",
    "name": "David Brown",
    "age": "forty-five",  # Should be int
    "readings": [2.1, "invalid", 1.8],  # Contains invalid reading
}

print("Testing valid data:")
if validate_patient_data(valid_data):
    print("  ✓ Data is valid")

print("\nTesting invalid data:")
if not validate_patient_data(invalid_data):
    print("  ✗ Data validation failed as expected")

# ============================================================
# Advanced Type Hints Features
# ============================================================

print("\n=== Advanced Type Hints ===")

# Type aliases for complex types
PatientID = str
InflammationReading = float
PatientRecord = Dict[str, Union[str, int, List[InflammationReading]]]


def process_patient_records(
    records: List[PatientRecord],
) -> Dict[PatientID, InflammationReading]:
    """Process patient records using type aliases."""
    results: Dict[PatientID, InflammationReading] = {}

    for record in records:
        patient_id: PatientID = str(record["patient_id"])
        readings: List[InflammationReading] = record.get("readings", [])

        if readings:
            avg: InflammationReading = sum(readings) / len(readings)
            results[patient_id] = avg

    return results


# Literal types (Python 3.8+)
if sys.version_info >= (3, 8):
    from typing import Literal

    RiskLevel = Literal["low", "medium", "high", "unknown"]

    def assess_risk(age: int, avg_inflammation: float) -> RiskLevel:
        """Assess patient risk with literal return type."""
        if age >= 65 and avg_inflammation > 5:
            return "high"
        elif avg_inflammation > 7:
            return "high"
        elif avg_inflammation > 3:
            return "medium"
        else:
            return "low"

    # Test literal types
    risk: RiskLevel = assess_risk(70, 6.5)
    print(f"Risk assessment: {risk}")

# Final types (Python 3.8+)
if sys.version_info >= (3, 8):
    from typing import Final

    MAX_INFLAMMATION: Final[float] = 20.0
    PATIENT_ID_PREFIX: Final[str] = "PAT_"

    print(f"Constants: MAX={MAX_INFLAMMATION}, PREFIX='{PATIENT_ID_PREFIX}'")

print("\n=== Type Hinting Best Practices ===")
best_practices = [
    "✓ Use type hints for function parameters and return values",
    "✓ Add type hints to class attributes in __init__",
    "✓ Use Optional for values that can be None",
    "✓ Use Union for parameters that accept multiple types",
    "✓ Use type aliases for complex type combinations",
    "✓ Use Generic for reusable code with multiple types",
    "✓ Validate types at runtime for critical data",
    "✓ Use mypy or similar tools for static type checking",
    "✓ Keep type hints simple and readable",
    "✓ Don't over-type - focus on important interfaces",
]

for practice in best_practices:
    print(f"  {practice}")

print("\n💡 Type hints improve code readability, IDE support, and catch errors early!")
print("💡 Use tools like mypy: 'pip install mypy && mypy your_script.py'")
