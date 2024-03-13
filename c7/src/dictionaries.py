from pprint import pprint


x = {'a': 1, 'b': 2}
print(x)

x['a'] = 3
print(x)

stocks = {
    "GOOG": (1235.20, 1242.54, 1231.06),
    "MSFT": (110.41, 110.45, 109.84),
}
stocks.setdefault("GOOG", "INVALID")

print(stocks.get("RIMM"))
print(stocks.get("RIMM", "Not found"))

for stock, values in stocks.items():
    print(f"{stock} last value is {values[0]}")

x = 2020
y = 2305843009213695971
print(hash(x) == hash(y))
print(x == y)

asd = {2020: 'a', 2305843009213695971: 'b'}
print(asd)
print(hash(frozenset(asd.items())))
pprint(asd)
