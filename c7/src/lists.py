from __future__ import annotations
from pprint import pprint
import string
from dataclasses import dataclass
from typing import Optional, cast, Any
import datetime

CHARACTERS = list(string.ascii_letters) + [" "]


def letter_frequency(sentence: str) -> list[tuple[str, int]]:
    frequencies = [(c, 0) for c in CHARACTERS]
    for letter in sentence:
        index = CHARACTERS.index(letter)
        frequencies[index] = (letter, frequencies[index][1] + 1)
    non_zero = [
        (letter, count)
        for letter, count in frequencies if count > 0
    ]
    return non_zero


print(letter_frequency('MMMario'))


@dataclass(frozen=True)
class MultiItem:
    data_source: str
    timestamp: Optional[float]
    creation_date: Optional[str]
    name: str
    owner_etc: str

    @property
    def datetime(self) -> datetime.datetime:
        if self.data_source == "Local":
            return datetime.datetime.fromtimestamp(
                cast(float, self.timestamp)
            )
        else:
            return datetime.datetime.fromisoformat(
                cast(str, self.creation_date)
            )

    def __lt__(self, other: Any) -> bool:
        if self.data_source == "Local":
            self_datetime = datetime.datetime.fromtimestamp(
                cast(float, self.timestamp)
            )
        else:
            self_datetime = datetime.datetime.fromisoformat(
                cast(str, self.creation_date)
            )
        if other.data_source == "Local":
            other_datetime = datetime.datetime.fromtimestamp(
                cast(float, other.timestamp)
            )
        else:
            other_datetime = datetime.datetime.fromisoformat(
                cast(str, other.creation_date)
            )
        return self_datetime < other_datetime


mi_0 = MultiItem("Local", 1607280522.68012, None, "Some File", "etc. 0")
mi_1 = MultiItem("Remote", None, "2020-12-06T13:47:52.849153",
                 "Another File", "etc. 1")
mi_2 = MultiItem("Local", 1579373292.452993, None, "This File", "etc. 2")
mi_3 = MultiItem("Remote", None, "2020-01-18T13:48:12.452993",
                 "That File", "etc. 3")

file_list = [mi_0, mi_1, mi_2, mi_3]
file_list.sort()
pprint(file_list)
