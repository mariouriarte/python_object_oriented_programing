from typing import (
    cast,
    Optional,
    Iterable
)
import datetime
from sample import Sample
import domain.specie_domain as specie
from exception.invalid_sample_error import InvalidSampleError


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
        # self.species = species
        self.species = specie.species_variable_iniciada.validate(species)

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"sepal_length = {self.sepal_length}, "
            f"sepal_width = {self.sepal_width}, "
            f"petal_length = {self.petal_length}, "
            f"petal_width = {self.petal_width}, "
            f"species = {self.species!r}, "
            f")"
        )

    @classmethod
    def from_dict(cls, row: dict[str, str]) -> "KnownSample":
        """Create KnownSample from dist csv info"""
        try:
            return cls(
                species=row["species"],
                sepal_length=float(row["sepal_length"]),
                sepal_width=float(row["sepal_width"]),
                petal_length=float(row["petal_length"]),
                petal_width=float(row["petal_width"]),
            )
        except ValueError:
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


class Hyperparameter:
    pass


class TrainingData:
    """A set of training data and testing data with methods to load and test the samples."""

    def __init__(self, name: str) -> None:
        self.name = name
        self.uploaded: datetime.datetime
        self.tested: datetime.datetime
        self.training: list[TrainingKnownSample] = []
        self.testing: list[TestingKnownSample] = []
        self.tuning: list[Hyperparameter] = []

    def load(self, raw_data_iter: Iterable[dict[str, str]]) -> None:
        """Extract TestingKnownSample and TrainingKnownSample from raw data"""
        bad_count = 0
        for n, row in enumerate(raw_data_iter):
            try:
                if n % 5 == 0:
                    test = TestingKnownSample.from_dict(row)
                    self.testing.append(test)
                else:
                    train = TrainingKnownSample.from_dict(row)
                    self.training.append(train)
            except InvalidSampleError as ex:
                print(f"Row {n+1}: {ex}")
                bad_count += 1
        if bad_count != 0:
            print(f"{bad_count} invalid rows")
            return
        self.uploaded = datetime.datetime.now(tz=datetime.timezone.utc)

    def __repr__(self) -> str:
        res = ''
        for s in self.testing:
            res += str(s) + "\n"
        for s in self.training:
            res += str(s) + "\n"
        return res


if __name__ == '__main__':
    valid = {"sepal_length": "5.1",
             "sepal_width": "3.5",
             "petal_length": "1.4",
             "petal_width": "0.2",
             "species": "Iris-setosa"}
    rks = TrainingKnownSample.from_dict(valid)
    # print(rks)

    invalid_species = {"sepal_length": "5.1", "sepal_width": "3.5",
                       "petal_length": "1.4", "petal_width": "0.2",
                       "species": "nothing known by this app"}
    # eks = TestingKnownSample.from_dict(invalid_species)

    trn_data = TrainingData('Mario')
    trn_data.load([
        invalid_species,
        valid,
        valid,
        valid,
        valid,
        valid,
        invalid_species,
        invalid_species
    ])
    print(trn_data)

    know_sample = KnownSample(
        "Iris-setosa",
        "5.1",
        "3.5",
        "1.4",
        "0.2",
    )
    print(know_sample)
