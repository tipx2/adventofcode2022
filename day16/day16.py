from parse import parse
import functools
import sys
with open("input16.txt") as f:
    lines = f.readlines()

valves = dict()
valves_values = dict()

for line in lines:
    x = parse("Valve {} has flow rate={}; tunnels lead to valves {}", line)
    if x == None:
        x = parse("Valve {} has flow rate={}; tunnel leads to valve {}", line)
    valves[x[0]] =  [y.strip() for y in x[2].strip().split(",")]
    valves_values[x[0]] = int(x[1])

# if minutes <= 0 return 0
# best = 0
# best = max(best, recursive loop through child nodes (minutes -1))
# if we haven't seen the current node and the rate isn't 0
# 	add current node to seen set
# 	take away a minute
# 	best = max(best, minutes * current node's rate + recursive loop through child nodes (minutes -1))
#   return best

sys.setrecursionlimit(10000)

@functools.cache
def part_one(seen, minutes, current, part):
    if minutes <= 0:
        return 0 if part == 1 else part_one(seen, 26, "AA", part=1)

    most_pressure = 0
    for child in valves[current]:
        most_pressure = max(most_pressure, part_one(seen, minutes-1, child, part))

    if current not in seen and valves_values[current] > 0 and minutes > 0:
        seen = set(seen)
        seen.add(current)
        minutes -= 1
        for child in valves[current]:
            most_pressure = max(most_pressure, minutes * valves_values[current] + part_one(frozenset(seen), minutes-1, child, part))
    return most_pressure
    
print(part_one(frozenset(), 30, "AA", part=1))
print(part_one(frozenset(), 26, "AA", part=2))