import argparse
import shutil

from condition import Manager, FIRST, SECOND, THIRD, FOURTH, FIFTH
from dxf import DXFHandler

parser = argparse.ArgumentParser()
parser.add_argument('file', type=argparse.FileType('r'))

if __name__ == "__main__":
    args = parser.parse_args()
    original_file = args.file.name
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

