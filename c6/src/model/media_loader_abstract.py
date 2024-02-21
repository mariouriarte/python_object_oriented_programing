import abc


class MediaLoaderAbstract(abc.ABC):
    @abc.abstractmethod
    def play(self) -> None:
        ...

    @property
    @abc.abstractmethod
    def ext(self) -> str:
        ...

    def asd(self) -> str:
        print('asd')

from collections.abc import Container
print(Container.__abstractmethods__)
#help(Container.__contains__)

class OddIntegers:
    def __contains__(self, x: int) -> bool:
        return x % 2 != 0
    
odd = OddIntegers()
print(isinstance(odd, Container))
print(issubclass(OddIntegers, Container))

print(1 in odd)
print(2 in odd)
print(3 in odd)