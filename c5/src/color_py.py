class Color_VP:
    def __init__(self, rgb: int, name: str) -> None:
        self._rgb_value = rgb
        # if not name:
        #     raise ValueError(f"Invalid name {name!r}")
        self._name: str = None
        self._set_name(name)


    def _set_name(self, name: str) -> None:
        if not name:
            raise ValueError(f"Invalid name {name!r}")
        self._name = name

    def _get_name(self) -> str:
        return self._name

    name = property(_get_name, _set_name)


if __name__ == "__main__":
    c = Color_VP(0xff0000, "bright red")
    print(c.name)

    c.name = "red"
    print(c.name)

    # c.name = ""
    c._name = "asd"
    print(c.name)
