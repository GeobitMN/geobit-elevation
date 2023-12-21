from condition import Manager, FIRST, SECOND, THIRD, FOURTH, FIFTH
from dxf import DXFHandler


if __name__ == "__main__":
    file_location = "./res/SIATKA_5x5cm_POLILINIE_3DPUNKTY_TEST_1.dxf"

    handler = DXFHandler(file_location=file_location)
    layer = handler.create_new_layer("test_layer")
    lines = handler.lines

    manager = Manager(
        handler=handler,
        lines=lines,
        condition=FIRST
    )

    manager.run_calculations()

