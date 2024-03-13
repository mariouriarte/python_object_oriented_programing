from __future__ import annotations
from dataclasses import dataclass
from collections import defaultdict
from typing import collections
from pprint import pprint


def letter_frequency(sentence: str) -> dict[str, int]:
    frequencies: dict[str, int] = {}
    for letter in sentence:
        frequency = frequencies.setdefault(letter, 0)
        frequencies[letter] = frequency + 1
    return frequencies


print(letter_frequency('aaaaaasdfghjkl'))


def letter_frequency_2(sentence: str) -> defaultdict[str, int]:
    frequencies: defaultdict[str, int] = defaultdict(int)
    for letter in sentence:
        frequencies[letter] += 1
    return frequencies


print(letter_frequency_2('aaaaaasdfghjklaa'))


@dataclass
class Prices:
    current: float = 0.0
    high: float = 0.0
    low: float = 0.0


portfolio = collections.defaultdict(Prices)
print(portfolio)
print(portfolio["GOOG"])
portfolio["AAPL"] = Prices(current=122.25, high=137.98, low=53.15)
print(portfolio["AAPL"])
pprint(portfolio)
