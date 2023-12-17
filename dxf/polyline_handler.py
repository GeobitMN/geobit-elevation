from .point_handler import PointHandler


class PolylineHandler:
    def __init__(self, line):
        self._line = line

    @property
    def line(self):
        return self._line

    @property
    def vertices(self):
        for vertex in self._line.vertices:
            yield PointHandler(vertex=vertex)
