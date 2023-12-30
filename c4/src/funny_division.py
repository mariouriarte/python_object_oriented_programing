from typing import Union

def funny_division(divisor: float) -> Union[str, float]:
    print('division two numbers')
    try:
        if divisor == 13:
            raise ValueError("13 is an unlucky number")
        return 100 / divisor
    except ZeroDivisionError:
        return "Zero is not a good idea!"

# print(funny_division(0))
# print(funny_division('hello'))

def funnier_division(divisor: int) -> Union[str, float]:
    try:
        if divisor == 13:
            raise ValueError("13 is an unlucky number")
        return 100 / divisor
    except (ZeroDivisionError, TypeError):
        return "Enter a number other than zero"

# for val in (0, "hello", 50.0, 13):
#     print(f"Testing {val!r}:", end=" ")
#     print(funnier_division(val))

def funniest_division(divisor: int) -> Union[str, float]:
    try:
        if divisor == 13:
            raise ValueError("13 is an unlucky number")
        return 100 / divisor
    except ZeroDivisionError:
        return "Enter a number other than zero"
    except TypeError:
        return "Enter a numerical value"
    except ValueError:
        print("No, No, not 13!")
        raise

try:
    raise ValueError("This is an argument")
except ValueError as e:
    print(f"The exception arguments were {e.args}")
