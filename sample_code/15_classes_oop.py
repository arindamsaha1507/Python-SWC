# Episode 15: Object-Oriented Programming in Python
# Sample code demonstrating OOP concepts for scientific Python programming

import math
import json
from datetime import datetime, date
from typing import List, Dict, Optional, Union, Any, Tuple
from abc import ABC, abstractmethod
from enum import Enum
import copy

# ============================================================
# Basic Class Definition and Instantiation
# ============================================================

print("=== Basic Classes and Objects ===")


class Patient:
    """Basic Patient class demonstrating class fundamentals."""

    # Class variables (shared by all instances)
    species = "Homo sapiens"
    total_patients = 0

    def __init__(self, patient_id: str, name: str, age: int, weight: float = None):
        """Initialize a new patient."""
        # Instance variables (unique to each instance)
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.weight = weight
        self.inflammation_readings = []
        self.created_at = datetime.now()

        # Update class variable
        Patient.total_patients += 1

    def add_inflammation_reading(self, reading: float) -> None:
        """Add an inflammation reading."""
        if reading < 0:
            raise ValueError("Inflammation reading cannot be negative")
        self.inflammation_readings.append(reading)

    def get_average_inflammation(self) -> Optional[float]:
        """Calculate average inflammation."""
        if not self.inflammation_readings:
            return None
        return sum(self.inflammation_readings) / len(self.inflammation_readings)

    def __str__(self) -> str:
        """String representation for users."""
        avg = self.get_average_inflammation()
        avg_str = f"{avg:.2f}" if avg is not None else "N/A"
        return f"Patient {self.patient_id}: {self.name} (avg inflammation: {avg_str})"

    def __repr__(self) -> str:
        """String representation for developers."""
        return f"Patient('{self.patient_id}', '{self.name}', {self.age})"


# Create and use basic patient objects
print("Creating patients...")
patient1 = Patient("P001", "Alice Johnson", 45, 65.5)
patient2 = Patient("P002", "Bob Smith", 52, 78.2)

print(f"Total patients created: {Patient.total_patients}")
print(f"Patient species: {Patient.species}")

# Add some readings
patient1.add_inflammation_reading(2.1)
patient1.add_inflammation_reading(3.4)
patient1.add_inflammation_reading(1.8)

patient2.add_inflammation_reading(5.2)
patient2.add_inflammation_reading(4.1)

print(f"Patient 1: {patient1}")
print(f"Patient 2: {patient2}")
print(f"Patient 1 repr: {repr(patient1)}")

# ============================================================
# Properties and Encapsulation
# ============================================================

print("\n=== Properties and Encapsulation ===")


class SecurePatient:
    """Patient class demonstrating encapsulation and properties."""

    def __init__(self, patient_id: str, name: str, age: int):
        self._patient_id = patient_id  # Protected attribute
        self._name = name
        self._age = age
        self.__social_security = None  # Private attribute
        self._inflammation_readings = []

    @property
    def patient_id(self) -> str:
        """Patient ID property (read-only)."""
        return self._patient_id

    @property
    def name(self) -> str:
        """Patient name property."""
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """Set patient name with validation."""
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = value.strip()

    @property
    def age(self) -> int:
        """Patient age property."""
        return self._age

    @age.setter
    def age(self, value: int) -> None:
        """Set patient age with validation."""
        if not isinstance(value, int) or value < 0 or value > 150:
            raise ValueError("Age must be between 0 and 150")
        self._age = value

    @property
    def inflammation_count(self) -> int:
        """Number of inflammation readings (computed property)."""
        return len(self._inflammation_readings)

    @property
    def average_inflammation(self) -> Optional[float]:
        """Average inflammation (computed property)."""
        if not self._inflammation_readings:
            return None
        return sum(self._inflammation_readings) / len(self._inflammation_readings)

    def add_reading(self, reading: float) -> None:
        """Add inflammation reading with validation."""
        if not isinstance(reading, (int, float)) or reading < 0:
            raise ValueError("Reading must be a non-negative number")
        self._inflammation_readings.append(float(reading))

    def get_readings(self) -> List[float]:
        """Get copy of readings (protecting internal state)."""
        return self._inflammation_readings.copy()

    def _calculate_risk_score(self) -> float:
        """Protected method for internal calculations."""
        if not self._inflammation_readings:
            return 0.0

        avg = self.average_inflammation
        age_factor = self._age / 100.0
        return avg * (1 + age_factor)

    def __set_social_security(self, ssn: str) -> None:
        """Private method - name mangled to prevent external access."""
        self.__social_security = ssn


# Test properties and encapsulation
secure_patient = SecurePatient("SP001", "Carol Wilson", 38)

print(f"Patient ID: {secure_patient.patient_id}")
print(f"Initial name: {secure_patient.name}")

# Test property setters
secure_patient.name = "Carol Ann Wilson"
secure_patient.age = 39

print(f"Updated name: {secure_patient.name}")
print(f"Updated age: {secure_patient.age}")

# Add readings and test computed properties
secure_patient.add_reading(1.5)
secure_patient.add_reading(2.8)
secure_patient.add_reading(3.1)

print(f"Inflammation count: {secure_patient.inflammation_count}")
print(f"Average inflammation: {secure_patient.average_inflammation:.2f}")

# Test validation
try:
    secure_patient.age = -5  # Should raise ValueError
except ValueError as e:
    print(f"Validation error: {e}")

# ============================================================
# Inheritance and Method Overriding
# ============================================================

print("\n=== Inheritance and Polymorphism ===")


class Person:
    """Base class for all people."""

    def __init__(self, name: str, age: int, contact_info: str = ""):
        self.name = name
        self.age = age
        self.contact_info = contact_info

    def introduce(self) -> str:
        """Introduce the person."""
        return f"Hello, I'm {self.name}, {self.age} years old."

    def get_info(self) -> Dict[str, Any]:
        """Get person information."""
        return {
            "name": self.name,
            "age": self.age,
            "type": "Person",
            "contact": self.contact_info,
        }


class StudyParticipant(Person):
    """Study participant - inherits from Person."""

    def __init__(
        self,
        name: str,
        age: int,
        participant_id: str,
        study_group: str,
        contact_info: str = "",
    ):
        super().__init__(name, age, contact_info)  # Call parent constructor
        self.participant_id = participant_id
        self.study_group = study_group
        self.inflammation_data = []
        self.enrollment_date = date.today()

    def introduce(self) -> str:
        """Override introduce method."""
        base_intro = super().introduce()
        return f"{base_intro} I'm participant {self.participant_id} in the {self.study_group} group."

    def add_inflammation_data(self, daily_readings: List[float]) -> None:
        """Add a day's worth of inflammation readings."""
        self.inflammation_data.append(daily_readings.copy())

    def get_info(self) -> Dict[str, Any]:
        """Override get_info to include participant-specific data."""
        info = super().get_info()
        info.update(
            {
                "type": "StudyParticipant",
                "participant_id": self.participant_id,
                "study_group": self.study_group,
                "enrollment_date": self.enrollment_date.isoformat(),
                "days_of_data": len(self.inflammation_data),
            }
        )
        return info


class Researcher(Person):
    """Researcher - another Person subclass."""

    def __init__(
        self,
        name: str,
        age: int,
        employee_id: str,
        department: str,
        specialization: str,
        contact_info: str = "",
    ):
        super().__init__(name, age, contact_info)
        self.employee_id = employee_id
        self.department = department
        self.specialization = specialization
        self.assigned_participants = []

    def introduce(self) -> str:
        """Override introduce method."""
        base_intro = super().introduce()
        return f"{base_intro} I'm Dr. {self.name}, researching {self.specialization}."

    def assign_participant(self, participant: StudyParticipant) -> None:
        """Assign a participant to this researcher."""
        self.assigned_participants.append(participant)

    def get_participant_summary(self) -> Dict[str, Any]:
        """Get summary of assigned participants."""
        groups = {}
        total_data_points = 0

        for participant in self.assigned_participants:
            group = participant.study_group
            if group not in groups:
                groups[group] = 0
            groups[group] += 1
            total_data_points += len(participant.inflammation_data)

        return {
            "total_participants": len(self.assigned_participants),
            "groups": groups,
            "total_data_points": total_data_points,
        }

    def get_info(self) -> Dict[str, Any]:
        """Override get_info."""
        info = super().get_info()
        info.update(
            {
                "type": "Researcher",
                "employee_id": self.employee_id,
                "department": self.department,
                "specialization": self.specialization,
                "assigned_participants": len(self.assigned_participants),
            }
        )
        return info


# Test inheritance
participant = StudyParticipant("David Brown", 29, "SP101", "control", "david@email.com")
researcher = Researcher(
    "Dr. Sarah Lee",
    45,
    "E001",
    "Medical Research",
    "Inflammation Studies",
    "sarah@university.edu",
)

print("=== Polymorphism Demo ===")
people = [participant, researcher]

for person in people:
    print(f"Introduction: {person.introduce()}")
    print(f"Info: {person.get_info()}")
    print()

# Test specific functionality
participant.add_inflammation_data([1.2, 2.1, 1.8, 2.5])
participant.add_inflammation_data([1.5, 2.3, 2.0, 2.8])

researcher.assign_participant(participant)
summary = researcher.get_participant_summary()
print(f"Researcher participant summary: {summary}")

# ============================================================
# Abstract Base Classes and Interfaces
# ============================================================

print("\n=== Abstract Base Classes ===")


class DataProcessor(ABC):
    """Abstract base class for data processors."""

    def __init__(self, name: str):
        self.name = name
        self.processed_count = 0

    @abstractmethod
    def process_data(self, data: List[float]) -> List[float]:
        """Process data - must be implemented by subclasses."""
        pass

    @abstractmethod
    def get_processing_info(self) -> Dict[str, Any]:
        """Get processing information - must be implemented by subclasses."""
        pass

    def log_processing(self, input_size: int, output_size: int) -> None:
        """Common logging functionality."""
        self.processed_count += 1
        print(
            f"{self.name}: Processed {input_size} -> {output_size} items (total: {self.processed_count})"
        )


class InflammationNormalizer(DataProcessor):
    """Concrete implementation: normalizes inflammation data."""

    def __init__(self, max_value: float = 20.0):
        super().__init__("Inflammation Normalizer")
        self.max_value = max_value

    def process_data(self, data: List[float]) -> List[float]:
        """Normalize data to 0-1 range."""
        if not data:
            return []

        normalized = [min(value / self.max_value, 1.0) for value in data]
        self.log_processing(len(data), len(normalized))
        return normalized

    def get_processing_info(self) -> Dict[str, Any]:
        """Get normalizer information."""
        return {
            "processor_type": "Normalizer",
            "max_value": self.max_value,
            "processed_batches": self.processed_count,
        }


class InflammationSmoother(DataProcessor):
    """Concrete implementation: smooths inflammation data."""

    def __init__(self, window_size: int = 3):
        super().__init__("Inflammation Smoother")
        self.window_size = window_size

    def process_data(self, data: List[float]) -> List[float]:
        """Apply moving average smoothing."""
        if len(data) < self.window_size:
            return data.copy()

        smoothed = []
        half_window = self.window_size // 2

        for i in range(len(data)):
            start = max(0, i - half_window)
            end = min(len(data), i + half_window + 1)
            window_data = data[start:end]
            smoothed.append(sum(window_data) / len(window_data))

        self.log_processing(len(data), len(smoothed))
        return smoothed

    def get_processing_info(self) -> Dict[str, Any]:
        """Get smoother information."""
        return {
            "processor_type": "Smoother",
            "window_size": self.window_size,
            "processed_batches": self.processed_count,
        }


# Test abstract classes
sample_data = [0.5, 3.2, 1.8, 7.5, 2.1, 5.8, 1.2, 4.3]

processors = [
    InflammationNormalizer(max_value=10.0),
    InflammationSmoother(window_size=3),
]

print("Processing with different processors:")
for processor in processors:
    result = processor.process_data(sample_data)
    info = processor.get_processing_info()
    print(f"  {processor.name}: {[f'{x:.2f}' for x in result[:5]]}... (info: {info})")

# ============================================================
# Composition and Aggregation
# ============================================================

print("\n=== Composition and Aggregation ===")


class InflammationReading:
    """Represents a single inflammation reading."""

    def __init__(self, value: float, timestamp: datetime = None, location: str = ""):
        self.value = value
        self.timestamp = timestamp or datetime.now()
        self.location = location
        self.quality_score = self._calculate_quality()

    def _calculate_quality(self) -> float:
        """Calculate data quality score."""
        # Simple quality metric based on value reasonableness
        if 0 <= self.value <= 20:
            return 1.0
        elif self.value > 20:
            return max(0.0, 1.0 - ((self.value - 20) / 20))
        else:
            return 0.0

    def __str__(self) -> str:
        return f"Reading({self.value:.1f}, quality={self.quality_score:.2f})"


class DailyInflammationData:
    """Represents inflammation data for one day - composition example."""

    def __init__(self, date: date, patient_id: str):
        self.date = date
        self.patient_id = patient_id
        self.readings = []  # Composition: readings belong to this daily data
        self.notes = ""

    def add_reading(self, value: float, location: str = "") -> InflammationReading:
        """Add a reading to this day."""
        reading = InflammationReading(value, datetime.now(), location)
        self.readings.append(reading)
        return reading

    def get_average(self) -> Optional[float]:
        """Get average reading for the day."""
        if not self.readings:
            return None
        return sum(r.value for r in self.readings) / len(self.readings)

    def get_quality_score(self) -> float:
        """Get overall quality score for the day."""
        if not self.readings:
            return 0.0
        return sum(r.quality_score for r in self.readings) / len(self.readings)

    def __str__(self) -> str:
        avg = self.get_average()
        avg_str = f"{avg:.2f}" if avg is not None else "N/A"
        return f"DailyData({self.date}, {len(self.readings)} readings, avg={avg_str})"


class Study:
    """Represents a research study - aggregation example."""

    def __init__(self, study_id: str, title: str, principal_investigator: Researcher):
        self.study_id = study_id
        self.title = title
        self.principal_investigator = (
            principal_investigator  # Aggregation: researcher exists independently
        )
        self.participants = []  # Aggregation: participants exist independently
        self.data_collection = {}  # Composition: data belongs to study
        self.start_date = date.today()
        self.status = "active"

    def enroll_participant(self, participant: StudyParticipant) -> None:
        """Enroll a participant in the study."""
        if participant not in self.participants:
            self.participants.append(participant)
            self.data_collection[participant.participant_id] = []

    def add_daily_data(
        self, participant_id: str, daily_data: DailyInflammationData
    ) -> None:
        """Add daily data for a participant."""
        if participant_id not in self.data_collection:
            raise ValueError(f"Participant {participant_id} not enrolled in study")
        self.data_collection[participant_id].append(daily_data)

    def get_study_statistics(self) -> Dict[str, Any]:
        """Get overall study statistics."""
        total_days = sum(len(days) for days in self.data_collection.values())
        total_readings = 0
        total_quality = 0.0
        quality_count = 0

        for days in self.data_collection.values():
            for daily_data in days:
                total_readings += len(daily_data.readings)
                if daily_data.readings:
                    total_quality += daily_data.get_quality_score()
                    quality_count += 1

        avg_quality = total_quality / quality_count if quality_count > 0 else 0.0

        return {
            "study_id": self.study_id,
            "participants": len(self.participants),
            "total_days": total_days,
            "total_readings": total_readings,
            "average_quality": avg_quality,
            "pi_name": self.principal_investigator.name,
        }


# Test composition and aggregation
researcher = Researcher(
    "Dr. Amanda Chen", 42, "E002", "Clinical Research", "Pain Management"
)
study = Study("INFLAM-2024", "Inflammation Response Study", researcher)

# Create participants
participant1 = StudyParticipant("Emma Davis", 34, "SP201", "treatment")
participant2 = StudyParticipant("Frank Miller", 28, "SP202", "control")

# Enroll participants
study.enroll_participant(participant1)
study.enroll_participant(participant2)

# Add daily data
daily_data1 = DailyInflammationData(date.today(), "SP201")
daily_data1.add_reading(2.1, "knee")
daily_data1.add_reading(1.8, "elbow")
daily_data1.add_reading(3.2, "ankle")

daily_data2 = DailyInflammationData(date.today(), "SP202")
daily_data2.add_reading(1.5, "knee")
daily_data2.add_reading(2.3, "elbow")

study.add_daily_data("SP201", daily_data1)
study.add_daily_data("SP202", daily_data2)

print("Study statistics:")
stats = study.get_study_statistics()
for key, value in stats.items():
    print(f"  {key}: {value}")

# ============================================================
# Enums and Data Classes
# ============================================================

print("\n=== Enums and Data Classes ===")


class InflammationSeverity(Enum):
    """Enumeration for inflammation severity levels."""

    NONE = 0
    MILD = 1
    MODERATE = 2
    SEVERE = 3
    CRITICAL = 4

    @classmethod
    def from_value(cls, value: float) -> "InflammationSeverity":
        """Convert numeric value to severity enum."""
        if value == 0:
            return cls.NONE
        elif value <= 2:
            return cls.MILD
        elif value <= 5:
            return cls.MODERATE
        elif value <= 10:
            return cls.SEVERE
        else:
            return cls.CRITICAL

    def get_description(self) -> str:
        """Get human-readable description."""
        descriptions = {
            self.NONE: "No inflammation detected",
            self.MILD: "Mild inflammation - monitor",
            self.MODERATE: "Moderate inflammation - may need treatment",
            self.SEVERE: "Severe inflammation - treatment recommended",
            self.CRITICAL: "Critical inflammation - immediate treatment required",
        }
        return descriptions[self]


# Data class example (Python 3.7+)
try:
    from dataclasses import dataclass, field

    @dataclass
    class LabResult:
        """Data class for laboratory results."""

        patient_id: str
        test_name: str
        value: float
        units: str
        reference_range: Tuple[float, float]
        timestamp: datetime = field(default_factory=datetime.now)
        technician: str = ""

        def __post_init__(self):
            """Post-initialization processing."""
            self.severity = InflammationSeverity.from_value(self.value)

        def is_normal(self) -> bool:
            """Check if result is within reference range."""
            return self.reference_range[0] <= self.value <= self.reference_range[1]

        def get_deviation(self) -> float:
            """Get deviation from normal range."""
            if self.value < self.reference_range[0]:
                return self.value - self.reference_range[0]
            elif self.value > self.reference_range[1]:
                return self.value - self.reference_range[1]
            else:
                return 0.0

    # Test data class
    lab_result = LabResult(
        patient_id="P003",
        test_name="C-Reactive Protein",
        value=8.5,
        units="mg/L",
        reference_range=(0.0, 3.0),
        technician="Tech-001",
    )

    print(f"Lab result: {lab_result}")
    print(f"Is normal: {lab_result.is_normal()}")
    print(f"Deviation: {lab_result.get_deviation():.1f}")
    print(f"Severity: {lab_result.severity.get_description()}")

except ImportError:
    print("Dataclasses not available (requires Python 3.7+)")

# Test enums
test_values = [0.0, 1.5, 3.8, 7.2, 15.5]
print("\nInflammation severity classification:")
for value in test_values:
    severity = InflammationSeverity.from_value(value)
    print(f"  {value}: {severity.name} - {severity.get_description()}")

# ============================================================
# Design Patterns
# ============================================================

print("\n=== Design Patterns ===")


# Singleton Pattern
class DatabaseConnection:
    """Singleton pattern for database connection."""

    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not self._initialized:
            self.connection_string = "inflammation_study_db"
            self.connected = True
            self._initialized = True
            print(f"Database connection established: {self.connection_string}")

    def query(self, sql: str) -> List[Dict]:
        """Execute a query."""
        print(f"Executing query: {sql}")
        return [{"result": "mock_data"}]


# Factory Pattern
class AnalysisFactory:
    """Factory pattern for creating analysis objects."""

    @staticmethod
    def create_analyzer(analysis_type: str, **kwargs) -> DataProcessor:
        """Create analyzer based on type."""
        if analysis_type == "normalize":
            return InflammationNormalizer(kwargs.get("max_value", 20.0))
        elif analysis_type == "smooth":
            return InflammationSmoother(kwargs.get("window_size", 3))
        else:
            raise ValueError(f"Unknown analysis type: {analysis_type}")


# Observer Pattern
class InflammationMonitor:
    """Observer pattern for monitoring inflammation changes."""

    def __init__(self):
        self.observers = []
        self.current_reading = 0.0

    def add_observer(self, observer) -> None:
        """Add an observer."""
        self.observers.append(observer)

    def remove_observer(self, observer) -> None:
        """Remove an observer."""
        self.observers.remove(observer)

    def notify_observers(self, reading: float) -> None:
        """Notify all observers of reading change."""
        for observer in self.observers:
            observer.update(reading)

    def set_reading(self, reading: float) -> None:
        """Set new reading and notify observers."""
        old_reading = self.current_reading
        self.current_reading = reading
        print(f"Reading changed: {old_reading:.1f} -> {reading:.1f}")
        self.notify_observers(reading)


class AlertSystem:
    """Observer that sends alerts for high readings."""

    def __init__(self, threshold: float = 10.0):
        self.threshold = threshold

    def update(self, reading: float) -> None:
        """Respond to reading updates."""
        if reading > self.threshold:
            print(f"🚨 ALERT: High inflammation detected: {reading:.1f}")


class DataLogger:
    """Observer that logs all readings."""

    def __init__(self):
        self.log = []

    def update(self, reading: float) -> None:
        """Log the reading."""
        timestamp = datetime.now().strftime("%H:%M:%S")
        entry = f"{timestamp}: {reading:.1f}"
        self.log.append(entry)
        print(f"📝 Logged: {entry}")


# Test design patterns
print("=== Singleton Pattern ===")
db1 = DatabaseConnection()
db2 = DatabaseConnection()
print(f"Same instance: {db1 is db2}")

print("\n=== Factory Pattern ===")
normalizer = AnalysisFactory.create_analyzer("normalize", max_value=15.0)
smoother = AnalysisFactory.create_analyzer("smooth", window_size=5)
print(f"Created normalizer: {normalizer.get_processing_info()}")
print(f"Created smoother: {smoother.get_processing_info()}")

print("\n=== Observer Pattern ===")
monitor = InflammationMonitor()
alert_system = AlertSystem(threshold=8.0)
logger = DataLogger()

monitor.add_observer(alert_system)
monitor.add_observer(logger)

# Test with different readings
test_readings = [3.2, 5.1, 9.5, 2.8, 12.3]
for reading in test_readings:
    monitor.set_reading(reading)

print(f"Logger captured {len(logger.log)} entries")

# ============================================================
# Advanced OOP Features
# ============================================================

print("\n=== Advanced OOP Features ===")


# Context Managers
class InflammationDataFile:
    """Context manager for handling inflammation data files."""

    def __init__(self, filename: str, mode: str = "r"):
        self.filename = filename
        self.mode = mode
        self.file = None
        self.data = []

    def __enter__(self):
        """Enter context - open file."""
        print(f"Opening file: {self.filename}")
        try:
            self.file = open(self.filename, self.mode)
            if self.mode == "r":
                # Read inflammation data
                import csv

                reader = csv.reader(self.file)
                for row in reader:
                    self.data.append([float(x) for x in row if x.strip()])
        except FileNotFoundError:
            print(f"File not found: {self.filename}")
            self.data = [[1.0, 2.0, 3.0]]  # Mock data for demo
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exit context - clean up."""
        if self.file:
            self.file.close()
        print(f"Closed file: {self.filename}")
        return False  # Don't suppress exceptions


# Descriptors
class ValidatedAttribute:
    """Descriptor for validated attributes."""

    def __init__(self, min_value=None, max_value=None):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.name = name
        self.private_name = f"_{name}"

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.private_name, None)

    def __set__(self, obj, value):
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f"{self.name} must be >= {self.min_value}")
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f"{self.name} must be <= {self.max_value}")
        setattr(obj, self.private_name, value)


class ValidatedPatient:
    """Patient class using descriptors for validation."""

    age = ValidatedAttribute(min_value=0, max_value=150)
    weight = ValidatedAttribute(min_value=0, max_value=500)

    def __init__(self, patient_id: str, name: str, age: int, weight: float):
        self.patient_id = patient_id
        self.name = name
        self.age = age  # Uses descriptor
        self.weight = weight  # Uses descriptor


# Metaclasses (advanced)
class SingletonMeta(type):
    """Metaclass for implementing singleton pattern."""

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class ConfigurationManager(metaclass=SingletonMeta):
    """Configuration manager using metaclass singleton."""

    def __init__(self):
        self.settings = {
            "max_inflammation": 20.0,
            "alert_threshold": 10.0,
            "data_directory": "./data",
        }

    def get(self, key: str, default=None):
        return self.settings.get(key, default)

    def set(self, key: str, value) -> None:
        self.settings[key] = value


# Test advanced features
print("=== Context Manager ===")
with InflammationDataFile("nonexistent.csv") as data_file:
    print(f"Data loaded: {len(data_file.data)} rows")

print("\n=== Descriptors ===")
try:
    validated_patient = ValidatedPatient("VP001", "Test Patient", 25, 70.5)
    print(
        f"Created patient: age={validated_patient.age}, weight={validated_patient.weight}"
    )

    validated_patient.age = 30  # Valid
    validated_patient.weight = -10  # Should raise error
except ValueError as e:
    print(f"Validation error: {e}")

print("\n=== Metaclass Singleton ===")
config1 = ConfigurationManager()
config2 = ConfigurationManager()
print(f"Same configuration instance: {config1 is config2}")

config1.set("test_setting", "test_value")
print(f"Config setting from second instance: {config2.get('test_setting')}")

# ============================================================
# Best Practices Summary
# ============================================================

print("\n=== OOP Best Practices ===")

best_practices = [
    "✓ Use clear, descriptive class names (PascalCase)",
    "✓ Keep classes focused on single responsibility",
    "✓ Prefer composition over inheritance when possible",
    "✓ Use properties for computed values and validation",
    "✓ Implement __str__ and __repr__ for better debugging",
    "✓ Use abstract base classes to define interfaces",
    "✓ Apply SOLID principles (Single Responsibility, Open/Closed, etc.)",
    "✓ Use type hints for better code documentation",
    "✓ Implement proper error handling and validation",
    "✓ Use design patterns appropriately, not just because you can",
    "✓ Keep inheritance hierarchies shallow and logical",
    "✓ Use enums for related constants",
    "✓ Consider using dataclasses for simple data containers",
    "✓ Test classes thoroughly, including edge cases",
    "✓ Document classes and methods with docstrings",
]

for practice in best_practices:
    print(f"  {practice}")

print("\n=== When to Use OOP ===")
use_cases = [
    "🎯 Modeling real-world entities (Patient, Study, Equipment)",
    "🎯 Creating reusable components with shared behavior",
    "🎯 Managing complex state and interactions",
    "🎯 Building extensible systems with plugins or modules",
    "🎯 Implementing design patterns for common problems",
    "🎯 Creating APIs and frameworks for others to use",
    "🎯 Organizing large codebases with clear structure",
]

for use_case in use_cases:
    print(f"  {use_case}")

print(
    "\n💡 OOP is a powerful tool for organizing complex code and modeling real-world problems!"
)
print("💡 Balance OOP with functional programming - use the right tool for each job.")
