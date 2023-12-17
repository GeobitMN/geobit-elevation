class PointHandler:
    def __init__(self, vertex):
        self._vertex = vertex

    @property
    def vertex(self):
        return self._vertex

    @property
    def x(self):
        return self._vertex.dxf.location.x

    @property
    def y(self):
        return self._vertex.dxf.location.y

    @property
    def z(self):
        return self._vertex.dxf.location.z
