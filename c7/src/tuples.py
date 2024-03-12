from typing import NamedTuple
import datetime
stock = "AAPL", 123.52, 53.15, 137.98
stock2 = ("AAPL", 123.52, 53.15, 137.98)

print(stock)
print(stock[2])
print(stock[1:3])
print('----')

print(stock2)


def middle(stock, date):
    symbol, current, high, low = stock
    return (((high + low) / 2), date)


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
        return (self.high + self.low)/2


s2 = Stock("AAPL", 123.52, 137.98, 53.15)
print(s2)
print(f"high: {high(s2)}")
print(hash(s2))
print(f"middle: {s2.middle}")
print('----')

t = ("Relayer", ["Gates of Delirium", "Sound Chaser"])
t[1].append("To Be Over")
print(t)
# hash(t)
