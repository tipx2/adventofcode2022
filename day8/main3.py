import time
# 0 short tree, 9 tall tree


# PPPPPPART 1
with open("input8.txt") as f:
	lines = f.readlines()
t = time.time()
lines = [l.strip() for l in lines]
totalvis = 0
for x in range(len(lines)): # each line
	for y in range(len(lines[x])): # each letter
		if y == 0 or x == 0 or x == len(lines[x])-1 or y == len(lines[x])-1:
			# tree is on edge
			totalvis += 1
		else:
			# left-right
			if max([int(w) for w in lines[x][:y]]) < int(lines[x][y]):
				# visible from left
				totalvis += 1
			elif max([int(w) for w in lines[x][y+1:]]) < int(lines[x][y]):
				# visible from right
				totalvis += 1

			# up down
			elif max([int(w[y]) for w in lines[x+1:]]) < int(lines[x][y]):
				# visible from down
				totalvis += 1
			elif max([int(w[y]) for w in lines[:x]]) < int(lines[x][y]):
				# visible from up
				totalvis += 1
print(totalvis)
print(time.time()-t)