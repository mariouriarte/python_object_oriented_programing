from math import hypot
# from __future__ import annotations
from typing import Tuple, List

Point = Tuple[float, float]


def distance(p_1: Point, p_2: Point) -> float:
    return hypot(p_1[0] - p_2[0], p_1[1] - p_2[1])


Polygon = List[Point]


def perimeter(polygon: Polygon) -> float:
    pairs = zip(polygon, polygon[1:] + polygon[:1])
    return sum(
        distance(p1, p2) for p1, p2 in pairs
    )


if __name__ == "__main__":
    square = [(1, 1), (1, 2), (2, 2), (2, 1)]
    print(perimeter(square))
