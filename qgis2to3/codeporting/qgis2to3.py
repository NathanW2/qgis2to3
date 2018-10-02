#!/usr/bin/env python3
import sys, os
import qgis2to3.codeporting

import lib2to3.main

def main():
    sys.path.append(os.path.abspath(os.path.dirname(qgis2to3.codeporting.__file__)))

    sys.exit(lib2to3.main.main('qgis_fixes'))

if __name__ == "__main__":
    main()
