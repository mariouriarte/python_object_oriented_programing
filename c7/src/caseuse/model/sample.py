from dataclasses import dataclass, asdict
from typing import Optional


@dataclass(frozen=True)
class Sample:
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


@dataclass(frozen=True)
class KnownSample(Sample):
    species: str


# @dataclass
class TestingKnownSample(KnownSample):
    classification: Optional[str] = None


@dataclass(frozen=True)
class TrainingKnownSample(KnownSample):
    """Note: no classification instance variable available."""
    pass
