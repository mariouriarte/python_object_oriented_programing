from collections.abc import Container
import abc


class MediaLoaderAbstract(abc.ABC):
    @abc.abstractmethod
    def play(self) -> None:
        ...

    @property
    @abc.abstractmethod
    def ext(self) -> str:
        ...

    def method_whit_body(self) -> str:
        print('Print some thing')
        return 'Some thing'


class OddIntegers:
    def __contains__(self, x: int) -> bool:
        return x % 2 != 0


if __name__ == '__main__':
    print(Container.__abstractmethods__)
    print(MediaLoaderAbstract.__abstractmethods__)
    # help(Container.__contains__)
    # help(MediaLoaderAbstract)

    odd = OddIntegers()
    print(isinstance(odd, Container))
    print(issubclass(OddIntegers, Container))

    print(1 in odd)
    print(2 in odd)
    print(3 in odd)
