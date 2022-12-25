import sys

if len(sys.argv) == 2:
    file_t = sys.argv[1]
else:
    file_t = "input22.txt"

with open(file_t) as f:
    lines = f.read().split("\n\n")

cubemap = lines[0]
instructions = lines[1]