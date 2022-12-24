import sys

if len(sys.argv) == 2:
    file_t = sys.argv[1]
else:
    file_t = "input23.txt"

with open(file_t) as f:
    lines = f.readlines()

# give each elf a proposed coordinate in a dictionary of elfcoord: proposed coord
# when assigning, add the proposed to a set if it's not already in the set
# if it was already in the set, go through the elf dict and remove the elf that is proposing that move, and also don't make that move

elves = []

for x in range(len(lines)):
    for y in range(len(lines[x])):
        if lines[x][y] == "#":
            elves.append((x,y))

def check_for_north(w, v):
    if not ((w-1, v-1) in elves or (w-1, v) in elves or (w-1, v+1) in elves):
        return (w-1, v)

def check_for_south(w, v):
    if not ((w+1, v-1) in elves or (w+1, v) in elves or (w+1, v+1) in elves):
        return (w+1, v)

def check_for_west(w, v):
    if not ((w-1, v-1) in elves or (w, v-1) in elves or (w+1, v-1) in elves):
        return (w, v-1)

def check_for_east(w,v):
    if not ((w-1, v+1) in elves or (w, v+1) in elves or (w+1, v+1) in elves):
        return (w, v+1)


def find_proposed(elf, n):
    w = elf[0]
    v = elf[1]
    a = [check_for_north(w, v), check_for_south(w, v), check_for_west(w, v), check_for_east(w, v)]
    
    # no elves around or elves everywhere? don't move
    if not None in a or a == [None, None, None, None]:
        return "no moves"
    
    # otherwise, rotate the array n times
    for t in range(n):
        a = a[1:] + [a[0]]
    
    # get the first available move
    for item in a:
        if item:
            return item

def print_map(elves):
    top_most = sorted(elves, key=lambda item: item[0])[0][0]
    bottom_most = sorted(elves, key=lambda item: item[0])[-1][0]

    left_most = sorted(elves, key=lambda item: item[1])[0][1]
    right_most = sorted(elves, key=lambda item: item[1])[-1][1]

    for x in range(top_most, bottom_most+1):
        for y in range(left_most, right_most+1):
            if (x,y) in elves:
                print("#", end="")
            else:
                print(".", end="")
            if y == right_most:
                print("\n", end="")

n = 0
while True:
    print(n)
    maybe_moves = {}
    dont_move_here = set()
    for elf in elves:
        proposed = find_proposed(elf, n)
        if proposed in maybe_moves.values():
            dont_move_here.add(proposed)
        elif proposed != "no moves" and not proposed in dont_move_here:
            maybe_moves[elf] = proposed
    
    new_elves = []
    for elf in elves:
        if elf in maybe_moves and maybe_moves[elf] not in dont_move_here:
            new_elves.append(maybe_moves[elf])
        else:
            new_elves.append(elf)
    if elves == new_elves:
        print(n+1)
        break
    else:
        elves = new_elves
    n += 1
    

# top_most = sorted(elves, key=lambda item: item[0])[0][0]
# bottom_most = sorted(elves, key=lambda item: item[0])[-1][0]

# left_most = sorted(elves, key=lambda item: item[1])[0][1]
# right_most = sorted(elves, key=lambda item: item[1])[-1][1]

# print((1+abs(bottom_most - top_most)) * (1+abs(right_most - left_most)) - len(elves))