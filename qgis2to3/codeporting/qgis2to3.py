#!/usr/bin/env python3
import sys, os
import functools
import qgis2to3.codeporting

import lib2to3.main

import lib2to3.refactor

lib2to3.refactor._open_with_encoding = functools.partial(open, newline='')

def main():
    sys.path.append(os.path.abspath(os.path.dirname(qgis2to3.codeporting.__file__)))
    sys.exit(lib2to3.main.main('qgis_fixes'))

if __name__ == "__main__":
    main()
