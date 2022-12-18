with open("input17.txt") as f:
    instructions = f.read()
from functools import cache
from tqdm import tqdm
# chamber is 7 wide
# the floor is at global y=0
# the walls are at global x=0 and global x=8

# for x in range 2022:
# spawn blocks[loopnumber % len(blocks)] 
#   where there are 2 units between leftmost bit on the block and left wall
#   and 3 units between bottommost and highest current rock
#   translate the local coordinates from the blocks array into global coordinates

# while the block hasn't stopped moving:
#   push the block in the direction of the instruction
#       check if this would cause it to intersect with any coordinates in the stopped rock set
#       or if it would push it into a wall
#       if so, that movement doesn't happen

#   then, move the block down 1 row
#       if this causes the block to move into the floor or an already stationary rock stop the rock
#       add the global coordinates of each of its parts to the set of stopped rocks
# recalculate highest rock

# where bottom left corner of shape is (0,0]
blocks = [
    [[0,0], [1,0], [2,0], [3,0]], # line across
    [[1,0], [0,1], [1,1], [2,1], [1,2]], # cross
    [[0,0],[1,0],[2,0],[2,1],[2,2]], # backwards L
    [[0,0],[0,1],[0,2],[0,3]], # line up
    [[0,0],[0,1],[1,0],[1,1]] # square
]

cache = {}
highest_rock = 0
stopped_rock_coords = set()
n = 0

current = None
inst = None

for w in range(1_000_000_000_000):
    if w == 2022:
        print(highest_rock)
    
    if current != None:
        
        key = (w % len(blocks), n % len(instructions))
        if key in cache:
            loop, cached_highest = cache[key]
            divide, modulo = divmod(1_000_000_000_000-w, w-loop)
            if modulo == 0: 
                print(highest_rock + (highest_rock-cached_highest)*divide)
                break
        else: 
            cache[key] = w, highest_rock
    
    current = blocks[w % len(blocks)].copy()
    spawnpoint = [3, highest_rock + 4]
    for g in range(len(current)):
        current[g] = [current[g][0] + spawnpoint[0], current[g][1] + spawnpoint[1]]
    
    breaking = False
    while not breaking:
        inst = instructions[n % len(instructions)]
        if inst == "<":
            # push left
            temprock = [[x[0]-1, x[1]] for x in current]
        elif inst == ">":
            # push right
            temprock = [[x[0]+1, x[1]] for x in current]
        
        for r in temprock: # check if it's a legal move
            if tuple(r) in stopped_rock_coords or r[0] >= 8 or r[0] <= 0: 
                break
        else: # if it doesn't break
            current = temprock.copy()
        n += 1
        # now we've either made the move, or stayed still because we can't make it
        # attempt to move downward
        downwardtemp = [[x[0],x[1]-1] for x in current]
        for p in downwardtemp:
            if tuple(p) in stopped_rock_coords or p[1] == 0:
                # we hit rock bottom
                for t in current:
                    stopped_rock_coords.add(tuple(t))
                breaking = True
                break
        else:
            current = downwardtemp.copy()
    highest_rock = sorted(list(stopped_rock_coords), key=lambda item: item[1])[-1][1]