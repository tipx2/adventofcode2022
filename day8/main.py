import time
# 0 short tree, 9 tall tree

# PPPPPART 2
with open("input8.txt") as f:
	lines = f.readlines()
t = time.time()

def gothrough(iter, currentitem):
	for w,i in enumerate(iter):
		if int(i) >= int(currentitem):
			return w+1
	return len(iter)

lines = [l.strip() for l in lines]
highest_scenic = 0
for x in range(len(lines)): # each line
	for y in range(len(lines[x])): # each letter
		scenic = 1
		# left-right
		leftarr = [int(w) for w in lines[x][:y]]
		rightarr = [int(w) for w in lines[x][y+1:]]
		# up-down
		downarr = [int(w[y]) for w in lines[x+1:]]
		uparr = [int(w[y]) for w in lines[:x]]

		directionsarr = [rightarr, list(reversed(leftarr)), downarr, list(reversed(uparr))]
		for z in directionsarr:
			scenic *= gothrough(z, lines[x][y])

		if scenic > highest_scenic:
			highest_scenic = scenic

print(highest_scenic)
print(time.time()-t)