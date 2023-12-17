import ezdxf

from .polyline_handler import PolylineHandler


class DXFHandler:
    def __init__(self, file_location="./res/SIATKA_5x5cm_POLILINIE_3DPUNKTY_TEST_1.dxf"):
        try:
            self._doc = ezdxf.readfile(file_location)
        except IOError:
            print(f"Could not open DXF file from location {file_location}")
        except ezdxf.DXFStructureError:
            print(f"Invalid or corrupted DXF file.")

        self._space = self._doc.modelspace()

    def create_new_layer(self, layer_name=None, color=7, line_type="DASHED"):
        if not layer_name:
            raise ValueError("No layer_name specified!")

        new_layer = self._doc.layers.add(name=layer_name, color=color, linetype=line_type)
        return new_layer

    @property
    def lines(self):
        lines = self._space.query("POLYLINE")

        if not lines:
            raise ValueError("No POLYLINE found in space!")

        return [PolylineHandler(line=line) for line in lines]
