import os
import sys

name = sys.argv[1]

os.mkdir(name)
os.chdir(name)
pyfile = name + ".py"

open(pyfile, "x")
