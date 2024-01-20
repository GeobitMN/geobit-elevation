import argparse
import os
import shutil

from condition import (
    CalculationsError,
    Manager,
    FIRST,
    SECOND,
    THIRD,
    FOURTH,
    FIFTH
)
from dxf import DXFHandler

parser = argparse.ArgumentParser()
parser.add_argument('file', type=argparse.FileType('r'))

if __name__ == "__main__":
    args = parser.parse_args()
    original_file = args.file.name
    file_template = original_file[:-4]

    for condition in [FIFTH]:
        # Copy file for the condition
        copied_file = f"{file_template}_warunek_{condition.type}.dxf"
        shutil.copy2(src=original_file, dst=copied_file)

        # Initialize for current condition
        handler = DXFHandler(file_location=copied_file)
        lines = handler.lines

        manager = Manager(
            handler=handler,
            lines=lines,
            condition=condition
        )

        # Perform calculations
        try:
            manager.run_calculations()
        except CalculationsError:
            # Calculations for the given file are incomplete - remove the file
            os.remove(copied_file)

