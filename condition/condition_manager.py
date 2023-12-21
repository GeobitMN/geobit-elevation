from calculations import calculate_height, height_difference
from condition import Condition
from dxf import DXFHandler, PolylineHandler


class Manager:
    def __init__(self, *, handler: DXFHandler, lines: [PolylineHandler], condition: Condition):
        self.handler = handler
        self.lines = lines
        self.type = condition.type
        self.offset = condition.point_offset
        self.tolerance = condition.tolerance

    def run_calculations(self):
        for line in self.lines:
            length = len(line.vertices)
            first_index = 0
            second_index = first_index + self.offset  # Gives 2nd point with distance for the given condition
            middle_index = int(self.offset/2)

            while second_index < length:
                point_a = line[first_index]
                point_b = line[second_index]
                point_mid = line[middle_index]

                height = calculate_height(a=point_a, b=point_b)
                delta = height_difference(point=point_mid, height=height)

                print(delta)

                first_index += 1
                second_index += 1
                middle_index += 1

