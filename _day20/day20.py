from collections import deque
with open("test20.txt") as f:
    striplines = [h.strip() for h in f.readlines()]
    lines = [[int(y), striplines.index(y)] for y in striplines]


def find_item(n, arr, g):
    for y in range(len(arr)):
        if arr[y][g] == n:
            return y # returns index of item found
    print("item not found (huh?)")

for x in range(len(lines)):
    current_item_index = find_item(x, lines, 1)
    
    new_pos = lines[current_item_index][0] + lines.index(lines[current_item_index])
    
    if new_pos <= 0:
        new_pos = len(lines)-1 + new_pos
    elif new_pos > len(lines):
        new_pos = 1 + new_pos
    
    new_pos = new_pos % len(lines)
    
    lines.insert(new_pos, lines.pop(current_item_index))
    
    # print([y[0] for y in lines])
    # print([y[0] for y in lines] == test_tester[x])
    # print()
    


zero_index = find_item(0, lines, 0)
print(sum([lines[(zero_index+1000*i)%len(lines)][0] for i in [1,2,3]]))