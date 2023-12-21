from collections import namedtuple

Condition = namedtuple("Condition", ["type", "point_offset", "tolerance"])

FIRST = Condition(type=1, point_offset=2, tolerance=1)
SECOND = Condition(type=2, point_offset=20, tolerance=3)
THIRD = Condition(type=3, point_offset=80, tolerance=9)
FOURTH = Condition(type=4, point_offset=200, tolerance=12)
FIFTH = Condition(type=5, point_offset=300, tolerance=15)
