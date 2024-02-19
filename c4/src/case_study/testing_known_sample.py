from typing import (
    cast,
    Optional
)
from know_sample import KnownSample

class TestingKnownSample(KnownSample):
    """Testing data. A classifier can assign a species, which may or may not be correct."""

    def __init__(
        self,
        /,
        species: str,
        sepal_length: float,
        sepal_width: float,
        petal_length: float,
        petal_width: float,
        purpose: int,
        classification: Optional[str] = None,
    ) -> None:
        super().__init__(
            species=species,
            sepal_length=sepal_length,
            sepal_width=sepal_width,
            petal_length=petal_length,
            petal_width=petal_width,
            purpose=purpose,
        )
        self.classification = classification

    def matches(self) -> bool:
        return self.species == self.classification

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"sepal_length = {self.sepal_length}, "
            f"sepal_width = {self.sepal_width}, "
            f"petal_length = {self.petal_length}, "
            f"petal_width = {self.petal_width}, "
            f"species = {self.species!r}, "
            f"classification = {self.classification!r}, "
            f")"
        )

    @classmethod
    def from_dict(cls, row: dict[str, str]) -> "TestingKnownSample":
        return cast(TestingKnownSample, super().from_dict(row))

