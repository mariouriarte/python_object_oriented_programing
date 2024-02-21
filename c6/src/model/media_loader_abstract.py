import abc


class MediaLoaderAbstract(abc.ABC):
    @abc.abstractmethod
    def play(self) -> None:
        ...

    @property
    @abc.abstractmethod
    def ext(self) -> str:
        ...
