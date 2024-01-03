from alive_progress import alive_bar

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

    def calculate_point_rotation(self, point_a, point_b):
        # If both Y values are the same, we have a vertical line, hence the 90 deg
        a = point_a.y
        b = point_b.y

        # We can compare for exact value as they are on the same line
        return 0 if a == b else 90

    def run_calculations(self):
        with alive_bar(total=len(self.lines), title=f"Przetwarzanie warunku #{self.type}") as bar:
            for count, line in enumerate(self.lines, 1):
                # Get new layer on which we will store heights
                layer = self.handler.create_new_layer(layer_name=f"#{count} {line.vertices[0].layer_name}")

                # Keep track of calculated points
                height_points = []

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

                    # Store point
                    # Point is created as follows:
                    # We use the same X,
                    # Add the delta of height to the Y - to obtain a difference in elevation on plot
                    # And use Delta as Z for safekeeping.
                    height_point = (point_mid.x, point_mid.y + delta, delta)
                    height_points.append(height_point)

                    first_index += 1
                    second_index += 1
                    middle_index += 1

                if point_a == None or point_b == None:
                    break
                text_rotation = self.calculate_point_rotation(point_a=point_a, point_b=point_b)
                self.handler.store_polyline(layer_name=layer, points=height_points)
                self.handler.store_points(layer_name=layer, points=height_points, text_rotation=text_rotation)
                # print(height_points)
                bar()

