import datetime
from threading import Timer
from typing import Any
from urllib.request import urlopen


class URLPolling:
    def __init__(self, url: str) -> None:
        self.url = url
        self.contents = ""
        self.last_updated: datetime.datetime
        self.timer: Timer
        self.update()

    def update(self) -> None:
        self.contents = urlopen(self.url).read()
        self.last_updated = datetime.datetime.now()
        self.schedule()

    def schedule(self) -> None:
        self.timer = Timer(5, self.update)
        self.timer.daemon = True
        self.timer.start()

    def __getstate__(self) -> dict[str, Any]:
        pickleable_state = self.__dict__.copy()
        if "timer" in pickleable_state:
            del pickleable_state["timer"]
        return pickleable_state

    def __setstate__(self, pickleable_state: dict[str, Any]) -> None:
        self.__dict__ = pickleable_state
        self.schedule()


if __name__ == "__main__":
    import pickle
    poll = URLPolling("http://dusty.phillips.codes")
    pickle.dumps(poll)
