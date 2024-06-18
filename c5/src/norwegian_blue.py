class NorwegianBlue_P:
    def __init__(self, name: str) -> None:
        self._name = name
        self._state: str = None

    @property
    def silly(self) -> str:
        print(f"Getting {self._name}'s State")
        return self._state

    @silly.setter
    def silly(self, state: str) -> None:
        print(f"Setting {self._name}'s State to {state!r}")
        self._state = state

    @silly.deleter
    def silly(self) -> None:
        print(f"{self._name} is pushing up daisies!")
        del self._state

    @property
    def age(self) -> int:
        pass

    @age.setter
    def age(self, age: int) -> None:
        self.age = age


if __name__ == "__main__":
    x = NorwegianBlue_P('Mario')
    x.silly = 'Activo'
    print(x.silly)
    print(x._state)
    del x.silly
    # print(x.silly)
