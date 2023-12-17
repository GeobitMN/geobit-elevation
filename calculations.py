from dxf import PointHandler


def calculate_height(point_a: PointHandler = None, point_b: PointHandler = None) -> float:
    height = (point_a.z + point_b.z) / 2
    return height


def calculate_height_difference(point: PointHandler, height: float) -> float:
    difference = point.z - height
    return difference
