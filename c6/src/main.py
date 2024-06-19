str_ = 'hola mundo'
print(str_)
print(type(str_))
print(id(str_))

str_ = "segundo hola mumndo"
print(str_)
print(type(str_))
print(str_[0])
print(id(str_))

d = {1: "one", True: "true", False: "Asd", 0: "qwe"}
print(d)

from typing import Dict, Hashable, Any, Mapping, Iterable


class NoDupDict(Dict[Hashable, Any]):
    def __setitem__(self, key, value) -> None:
        if key in self:
            raise ValueError(f"duplicate {key!r}")
        super().__setitem__(key, value)


nd = NoDupDict()
nd["a"] = 1
# raise value error
#nd["a"] = 2

print(NoDupDict({"a": 42, "a": 3.14}))
