from condition import Manager, FIRST, SECOND, THIRD, FOURTH, FIFTH
from dxf import DXFHandler
import shutil


if __name__ == "__main__":
    original_file = "./res/SIATKA_5x5cm_POLILINIE_3D_TEST_2.dxf"
    file_template = original_file[:-4]

    for condition in [FIRST, SECOND, THIRD, FOURTH, FIFTH]:
        # Copy file for the condition
        copied_file = f"{file_template}_warunek_{condition.type}.dxf"
        shutil.copy2(src=original_file, dst=copied_file)

        handler = DXFHandler(file_location=copied_file)
        lines = handler.lines

        manager = Manager(
            handler=handler,
            lines=lines,
            condition=condition
        )

        manager.run_calculations()

