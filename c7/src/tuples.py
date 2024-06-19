from typing import NamedTuple
import datetime
from pprint import pprint

stock = "AAPL", 123.52, 53.15, 137.98
stock2 = ("AAPL", 123.52, 53.15, 137.98)

print(stock)
print(stock[2])
print(stock[1:3])
print('----')

print(stock2)

print("---- mutables in tuple")
list_1 = [1, 2, 3, (1, 2, 3)]
dict_1 = {1: "a", 2: "b"}
tuple_1 = (list_1, dict_1)
list_ref = tuple_1[0]
list_ref[0] = 222
pprint(tuple_1)
pprint(list_1)


def middle(stock_, date):
    symbol, current, high, low = stock_
    return ((high + low) / 2), date


print(middle(stock2, datetime.date(2024, 12, 4)))

a = 42,
print(a)

b = (42, 3.14), (2.718, 2.618),
print(b)


def high(stock):
    symbol, current, high, low = stock
    return high


print(high(stock))


class Stock(NamedTuple):
    symbol: str
    current: float
    high: float
    low: float

    @property
    def middle(self) -> float:
        return (self.high + self.low) / 2


s2 = Stock("AAPL", 123.52, 137.98, 53.15)
print(s2)
print(f"high: {high(s2)}")
print(hash(s2))
print(f"middle: {s2.middle}")
print('<---->')

t = ("Relayer", ["Gates of Delirium", "Sound Chaser"])
t[1].append("To Be Over")
print(t)
# hash(t)

# asd = {s2: 2}

t2 = (2, 1, 3)
print(hash(t2))
