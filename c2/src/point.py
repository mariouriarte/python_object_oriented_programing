import math

class Point:
    '''Represent a two dimension coordinates'''

    def __init__(self, x: float, y: float) -> None:
        self.move(x, y)

    def move(self, x: float, y: float) -> None:
        '''Moves cordinates'''
        self.x = x
        self.y = y

    def reset(self):
        '''Reset coordinates to 0'''
        self.move(0, 0)

    def calculate_distance(self, other: "Point") -> float:
        '''Calculate the distance betwen two points'''
        return math.hypot(self.x - other.x, self.y - other.y)

def main() -> None:
    p1 = Point(5, 4)
    p2 = Point(3, 6)

    # p1.x = 5
    # p1.y = 4
    # p2.x = 3
    # p2.y = 6

    print(p1.x, p1.y)
    print(p2.x, p2.y)
    #----
    p = Point(0, 0)
    p.reset()
    print(p.x, p.y)

    # talkin to yourself
    p2 = Point(0, 0)
    Point.reset(p2)
    print(p2.x, p2.y)

    # more arguments
    point1 = Point(0, 0)
    point2 = Point(0, 0)

    point1.reset()
    point2.move(5, 1)
    print(point2.calculate_distance(point1))
    assert point2.calculate_distance(point1) == point1.calculate_distance(point2)
    point1.move(3, 4)
    print(point1.calculate_distance(point2))

if __name__ == "__main__":
    main()
