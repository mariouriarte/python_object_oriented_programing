from sample import Sample
import domain.specie_domain as specie
from exception.invalid_sample_error import InvalidSampleError
from typing import cast, Optional

class KnownSample(Sample):
    "Known sample of petals"

    def __init__(
        self,
        species: str,
        sepal_length: float,
        sepal_width: float,
        petal_length: float,
        petal_width: float,
    ) -> None:
        super().__init__(
            sepal_length=sepal_length,
            sepal_width=sepal_width,
            petal_length=petal_length,
            petal_width=petal_width,
        )
        self.species = species

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"sepal_length={self.sepal_length}, "
            f"sepal_width={self.sepal_width}, "
            f"petal_length={self.petal_length}, "
            f"petal_width={self.petal_width}, "
            f"species={self.species!r}, "
            f")"
        )

    @classmethod
    def from_dict(cls, row: dict[str, str]) -> "KnownSample":
        """Create KnownSample from dist csv info"""
        try:
            return cls(
                species=specie.species.validate(row["species"]),
                sepal_length=float(row["sepal_length"]),
                sepal_width=float(row["sepal_width"]),
                petal_length=float(row["petal_length"]),
                petal_width=float(row["petal_width"]),
            )
        except ValueError as ex:
            raise InvalidSampleError(f"invalid {row!r}")

class TrainingKnownSample(KnownSample):
    @classmethod
    def from_dict(cls, row: dict[str, str]) -> "TrainingKnownSample":
        return cast(TrainingKnownSample, super().from_dict(row))

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
        classification: Optional[str] = None,
    ) -> None:
        super().__init__(
            species=species,
            sepal_length=sepal_length,
            sepal_width=sepal_width,
            petal_length=petal_length,
            petal_width=petal_width,
        )
        self.classification = classification

    def matches(self) -> bool:
        return self.species == self.classification

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"sepal_length={self.sepal_length}, "
            f"sepal_width={self.sepal_width}, "
            f"petal_length={self.petal_length}, "
            f"petal_width={self.petal_width}, "
            f"species={self.species!r}, "
            f"classification={self.classification!r}, "
            f")"
        )

    @classmethod
    def from_dict(cls, row: dict[str, str]) -> "TestingKnownSample":
        return cast(TestingKnownSample, super().from_dict(row))

if __name__ == '__main__':
    valid = {"sepal_length": "5.1", "sepal_width": "3.5",
             "petal_length": "1.4", "petal_width": "0.2",
             "species": "Iris-setosa"}
    rks = TrainingKnownSample.from_dict(valid)
    print(rks)
    invalid_species = {"sepal_length": "5.1", "sepal_width": "3.5",
                       "petal_length": "1.4", "petal_width": "0.2",
                       "species": "nothing known by this app"}
    eks = TestingKnownSample.from_dict(invalid_species)
