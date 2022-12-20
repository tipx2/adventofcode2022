import time
with open("input7.txt") as f:
	lines = f.readlines()

# {"dir":[size, [innerdir1, innerdir2]]}
dirvalues = {"/Root": [0, []]}
currentdir = "/Root"

t = time.time()
# PASS 1
# fill the dictionary in the format above, directories with an empty dirvalues[n][1] have no child directories
tenativedir = ""
for line in lines:
	line = line.strip()
	if line[0] == "$":
		# command
		if line == "$ cd /":
			currentdir = "/Root"
		elif line[2:4] == "cd":
			if line[5:7] == "..":
				tenativedir = ""
				currentdir = currentdir[:currentdir.rindex("/")]
			else:
				tenativedir = line[4:].strip()
		elif line[2:4] == "ls" and tenativedir != "":
			currentdir += "/" + tenativedir

	else:

		if currentdir not in dirvalues.keys():
			dirvalues[currentdir] = [0, []]

		if line[0:3] == "dir":
			# directory
			name = currentdir + "/" + line.split(" ")[1].strip()
			dirvalues[currentdir][1].append(name)
		else:
			# file
			value, name = line.split(" ")
			value = int(value)
			dirvalues[currentdir][0] += value

# PASS 2
# "from bottom up", go through nodes with no child directories, and add their values to the parents containing them. remove them from their parent's child directory lists

# calculated deepest directory = 11
for x in range(11):
	for node in dirvalues:
		if len(dirvalues[node][1]) == 0:
			# node has no children
			# therefore search through every node to find ones where that contain the node
			for dir in dirvalues:
				if node in dirvalues[dir][1]:
					dirvalues[dir][0] += dirvalues[node][0]
					dirvalues[dir][1].remove(node)


# part 1
def part_1():
	total = 0
	for value in dirvalues:
		if dirvalues[value][0] <= 100000:
			# add it :)
			total += dirvalues[value][0]
	print("Part 1:")
	print(total)
	print()


def part_2():
	space_needed = 30000000 - (70000000 - dirvalues["/Root"][0])
	potential_dirs = []
	for value in dirvalues:
		if dirvalues[value][0] >= space_needed:
			potential_dirs.append(dirvalues[value][0])
	print("Space needed:", space_needed)
	print("Part 2:")
	print(sorted(potential_dirs)[0])


part_1()
print(time.time() - t)
