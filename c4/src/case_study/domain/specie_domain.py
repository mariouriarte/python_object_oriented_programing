from typing import Set

class Domain(Set[str]):
    def validate(self, value: str) -> str:
        if value in self:
            return value
        raise ValueError(f"invalid {value!r}")

species_variable_iniciada = Domain({
    "Iris-setosa",
    "Iris-versicolour",
    "Iris-virginica"})

# print(species.validate("Iris-versicoddlour"))
