import time
with open("input12.txt") as f:
	lines = f.readlines()
t = time.time()
lines = [l.strip() for l in lines]

alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet2 = alphabet[::-1]

# node is a tuple (x,y)
def get_children(node):
	children = [] # aron marshall (not real!!!1)
	check_em = [(node[0], node[1]+1), (node[0],node[1]-1), (node[0]+1, node[1]), (node[0]-1, node[1])]

	if node[0] <= 0:
		check_em.remove((node[0]-1, node[1]))
	elif node[0] >= len(lines)-1:
		check_em.remove((node[0]+1, node[1]))

	if node[1] <= 0:
		check_em.remove((node[0], node[1]-1))
	elif node[1] >= len(lines[node[0]])-1:
		check_em.remove((node[0], node[1]+1))
		
	if lines[node[0]][node[1]] == "S":
		currletter = len(alphabet2)-1
	elif lines[node[0]][node[1]] == "E":
		currletter = 0
	else:
		currletter = alphabet2.index(lines[node[0]][node[1]])
		
	for xnode in check_em:
		if lines[xnode[0]][xnode[1]] == "S":
			tentletter = len(alphabet2)-1
		elif lines[xnode[0]][xnode[1]] == "E":
			tentletter = 0
		else:
			tentletter = alphabet2.index(lines[xnode[0]][xnode[1]])

		if (tentletter == 1+currletter) or (tentletter <= currletter):
			children.append(xnode)
	return children

big_costs = []


explore = {(20,55):[0, []]}
seen = []

while explore != {}:
	# sort that priority
	explore = {k:v for k, v in sorted(explore.items(), key=lambda item: item[1][0])}
	node = list(explore.keys())[0]
	cost = explore[node][0]
	path = explore[node][1]

	del explore[list(explore.keys())[0]]

	if lines[node[0]][node[1]] == "a":
		big_costs.append(cost)
	
	if not node in seen:
		for n in get_children(node):
			if not n in explore.keys() or cost+1 < explore[n][0]:
				explore[n] = [cost+1, path + [lines[n[0]][n[1]]]]
		seen.append(node)

print(time.time()-t)
print(sorted(big_costs)[0])
