from pprint import pprint
from dataclasses import dataclass


@dataclass
class Stock:
    symbol: str
    current: float = 0.0
    high: float = 0.0
    low: float = 0.0

class StockOrdinary:
    def __init__(self, name: str, current: float, high: float, low: float) -> None:
        self.name = name
        self.current = current
        self.high = high
        self.low = low


s = Stock("AAPL", 123.52, 137.98, 53.15)
s2 = Stock("AAPL", 123.52, 137.98, 53.15)
print(s == s2)
print(s)
print(f"current: {s.current}")
s.current = 122.25
print(f"current: {s.current}")
print(s)
print('----')

s_ord = StockOrdinary("AAPL", 123.52, 137.98, 53.15)
s_ord_2 = StockOrdinary("AAPL", 123.52, 137.98, 53.15)
print(s_ord)
print(s_ord == s_ord_2)
# ----


@dataclass(order=True)
class StockOrdered:
    name: str
    current: float = 0.0
    high: float = 0.0
    low: float = 0.0


stock_ordered1 = StockOrdered("GOOG", 1826.77, 1847.20, 1013.54)
stock_ordered2 = StockOrdered("GOOG")
stock_ordered3 = StockOrdered("GOOG", 1728.28, high=1733.18, low=1666.33)
print(stock_ordered1 < stock_ordered2)
print(stock_ordered1 > stock_ordered2)
pprint(sorted([stock_ordered1, stock_ordered2, stock_ordered3]))

# asd = {s: "a"}
# print(hash(s))
