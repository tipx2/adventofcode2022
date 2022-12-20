import sys

if len(sys.argv) == 2:
    file_t = sys.argv[1]
else:
    file_t = "input20.txt"

with open(file_t) as f:
    striplines = [h.strip() for h in f.readlines()]

    

def find_item(n, arr, g): # g=0 for find by item, g=1 for find by index
    for y in range(len(arr)):
        if arr[y][g] == n:
            return y

def do_part(n, g):
    lines = [[int(y) * g, i] for i, y in enumerate(striplines)]
    for _ in range(n):
        for x in range(len(lines)):
            current_item_index = find_item(x, lines, 1)
            lines.insert((lines[current_item_index][0] + current_item_index) % (len(lines)-1), lines.pop(current_item_index))
    zero_index = find_item(0, lines, 0)
    return sum([lines[(zero_index+1000*i)%len(lines)][0] for i in [1,2,3]])


print("part 1:")
print(do_part(1, 1))
print("part 2:")
print(do_part(10, 811589153))