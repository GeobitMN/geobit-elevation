from .point_handler import PointHandler


class PolylineHandler:
    def __init__(self, line):
        self._line = line
        self._vertices = [PointHandler(vertex=vertex) for vertex in self._line.vertices]

    @property
    def line(self):
        return self._line

    @property
    def vertices(self):
        return self._vertices

    def __getitem__(self, index):
        return self._vertices[index]
