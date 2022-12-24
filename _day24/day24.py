import sys
import random
from copy import deepcopy

if len(sys.argv) == 2:
    file_t = sys.argv[1]
else:
    file_t = "input24.txt"

with open(file_t) as f:
    lines = f.readlines()

# current = set((dir, (x,y)), (dir, (x,y)))
# future_positions = set((x,y), (x,y))

blizzards = set()
for x in range(len(lines)):
    lines[x] = lines[x].strip()
    for y in range(len(lines[x])):
        if lines[x][y] == ">":
            blizzards.add(((0, 1), (x,y)))
        elif lines[x][y] == "<":
            blizzards.add(((0, -1), (x,y)))
        elif lines[x][y] == "V":
            blizzards.add(((1, 0), (x,y)))
        elif lines[x][y] == "^":
            blizzards.add(((-1, 0), (x,y)))

lenx = len(lines[0])
leny = len(lines)
saved_blizzards = deepcopy(blizzards)

me_start = (0, 1)
if file_t == "input24.txt":
    end = (26, 120)
elif file_t == "test24.txt":
    end = (6, 5)

def find_future(blizz):
    r = (blizz[0][0] + blizz[1][0], blizz[0][1] + blizz[1][1])
    if r[0] < 0 or r[0] > lenx:
        return
    if r[1] < 0 or r[1] > leny:
        return
    return r

def get_nearby_moveable_tiles(me, blizzards):
    plausable_tiles = [(-1+me[0],0+me[1]), (1+me[0],0+me[1]),(0+me[0],-1+me[1]),(0+me[0],1+me[1])]
    for t in plausable_tiles.copy():
        if t[0] < 0 or t[0] > lenx:
            plausable_tiles.remove(t)
        if t[1] < 0 or t[1] > leny:
            plausable_tiles.remove(t)
    
    future_positions = [find_future(blizz) for blizz in blizzards]
    for tile in plausable_tiles:
        