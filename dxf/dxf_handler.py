import ezdxf

from .polyline_handler import PolylineHandler


class DXFHandler:
    def __init__(self, file_location=None):
        try:
            self._doc = ezdxf.readfile(file_location)
        except IOError:
            print(f"Could not open DXF file from location {file_location}")
        except ezdxf.DXFStructureError:
            print(f"Invalid or corrupted DXF file.")

        self._space = self._doc.modelspace()

    def _save(self):
        self._doc.save()

    def create_new_layer(self, *, layer_name=None, color=7, line_type="CONTINUOUS"):
        if not layer_name:
            raise ValueError("No layer_name specified!")

        self._doc.layers.add(name=layer_name, color=color, linetype=line_type)
        return layer_name

    def store_polyline(self, *, layer_name=None, points=None):
        if not layer_name:
            raise ValueError("No layer_name specified!")

        if not points:
            raise ValueError("No points for polyline provided!")

        attribs = {"layer": layer_name}

        self._space.add_polyline3d(points=points, dxfattribs=attribs)
        self._save()

    def store_points(self, *, layer_name=None, points=None, text_rotation=0):
        if not layer_name:
            raise ValueError("No layer_name specified!")

        if not points:
            raise ValueError("No points provided!")

        attribs = {
            "layer": layer_name,
            "color": 62,
            "angle": 50,
            "plotstyle_enum": 380,
            "plotstyle_handle": 390,
        }

        for point in points:
            point_text = f"{(point[2] * 1000):.1f}"
            self._space.add_point(location=point, dxfattribs=attribs)
            self._space.add_text(text=point_text, height=0.005, rotation=text_rotation).set_placement(point)

        self._save()

    @property
    def lines(self):
        lines = self._space.query("POLYLINE")

        if not lines:
            raise ValueError("No POLYLINE found in space!")

        return [PolylineHandler(line=line) for line in lines]

    @property
    def points(self):
        points = self._space.query("POINT")

        if not points:
            raise ValueError("No POINT found in space!")

        return points.entities
