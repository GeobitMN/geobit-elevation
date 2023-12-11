import sys
import ezdxf


if __name__ == "__main__":
    try:
        doc = ezdxf.readfile("./res/SIATKA_5x5cm_POLILINIE_3DPUNKTY_TEST_1.dxf")
    except IOError:
        print(f"Not a DXF file or a generic I/O error.")
        sys.exit(1)
    except ezdxf.DXFStructureError:
        print(f"Invalid or corrupted DXF file.")
        sys.exit(2)

    msp = doc.modelspace()
    print(msp)
    lines = msp.query("POINT")
    print(lines)
