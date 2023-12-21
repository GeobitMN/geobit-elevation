from dxf import PointHandler


def calculate_height(a: PointHandler = None, b: PointHandler = None) -> float:
    height = (a.z + b.z) / 2
    return height


def height_difference(point: PointHandler, height: float) -> float:
    difference = point.z - height
    return difference
