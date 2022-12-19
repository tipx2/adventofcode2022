with open("input18.txt") as f:
    lines = f.readlines()

lines = [tuple([int(y) for y in x.split(",")]) for x in lines]

highest_coord = 0
for coord in lines:
    m = max(coord)
    if m > highest_coord:
        highest_coord = m

total_surface_area = 0
for cube in lines:
    total_surface_area += 6
    for neighbor_tuple in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0), (0,0,1),(0,0,-1)]:
        check = tuple(map(lambda x, y: x + y, cube, neighbor_tuple))
        if check in lines:
            total_surface_area -= 1
print("part 1:")     
print(total_surface_area)

external_surface_area = 0
queue = [(-highest_coord-1,-highest_coord-1,-highest_coord-1)]
seen = set()
# check all adjacent guys. if they are in lines, add 1 for each of them. add all air to the queue.
while queue != []:
        c = queue.pop(0)
        if c not in lines:
            for neighbor_tuple in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0), (0,0,1),(0,0,-1)]:
                check = tuple(map(lambda x, y: x + y, c, neighbor_tuple))
                if check in lines:
                    external_surface_area += 1
                else:
                    if not check in seen and check[0] <= highest_coord+2 and check[1] <= highest_coord+2 and check[2] <= highest_coord+2 and check[0] >= -highest_coord-2 and check[1] >= -highest_coord-2 and check[2] >= -highest_coord-2:
                        queue.append(check)
                        seen.add(check)


print("part 2:")
print(external_surface_area)