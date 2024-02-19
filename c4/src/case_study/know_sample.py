from typing import Optional
from sample import Sample
import domain.specie_domain as specie
from exception.invalid_sample_error import InvalidSampleError
from model.enum_purpose import Purpose


class KnownSample(Sample):
    "Known sample of petals"

    def __init__(
        self,
        sepal_length: float,
        sepal_width: float,
        petal_length: float,
        petal_width: float,
        species: str,
        purpose: int,
    ) -> None:
        purpose_enum = Purpose(purpose)
        if purpose_enum not in {Purpose.TRAINING, Purpose.TESTING}:
            raise ValueError(
                f"Invalid purpose: {purpose!r}: {purpose_enum}"
            )
        self.purpose = purpose_enum
        super().__init__(
            sepal_length=sepal_length,
            sepal_width=sepal_width,
            petal_length=petal_length,
            petal_width=petal_width,
        )
        self.species = specie.species_variable_iniciada.validate(species)
        self._classification: Optional[str] = None

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"sepal_length = {self.sepal_length}, "
            f"sepal_width = {self.sepal_width}, "
            f"petal_length = {self.petal_length}, "
            f"petal_width = {self.petal_width}, "
            f"species = {self.species!r}, "
            f"purpose = {self.purpose!r}, "
            f")"
        )

    def matches(self) -> bool:
        return self.species == self.classification

    @property
    def classification(self) -> Optional[str]:
        if self.purpose == Purpose.TESTING:
            return self._classification
        raise AttributeError("Training samples have no classification")

    @classification.setter
    def classification(self, value: str) -> None:
        if self.purpose == Purpose.TESTING:
            self._classification = value
        else:
            raise AttributeError("Training samples cannot be classified")

    @classmethod
    def from_dict(cls, row: dict[str, str]) -> "KnownSample":
        """Create KnownSample from dist csv info"""
        try:
            return cls(
                sepal_length=float(row["sepal_length"]),
                sepal_width=float(row["sepal_width"]),
                petal_length=float(row["petal_length"]),
                petal_width=float(row["petal_width"]),
                species=row["species"],
                purpose=int(row["purpose"]),
            )
        except ValueError:
            raise InvalidSampleError(f"invalid {row!r}")
            
