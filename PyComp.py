import py_compile as ppcc
import sys

try:
    ppcc.compile(sys.argv[1])
except:
    print("Error during compiling...\nPyComp failed.")
