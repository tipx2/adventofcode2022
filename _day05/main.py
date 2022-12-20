with open("input5.txt") as f:
	lines = f.read().split("\n\n")

bags = lines[0].split("\n")
instructs = lines[1].split("\n")

# parsing
bagdict = [[], [],[],[],[],[],[],[],[]]
for bag in reversed(bags):
	bag = bag.strip("[]")
	for x in range(0, len(bag)):
		if bag[x].isalpha():
			bagdict[x//4].append(bag[x])



def move(stackfrom, stackto, stackrange):
	temparr = []
	stackfrom -= 1
	stackto -= 1
	for x in range(stackrange):
		temparr.append(bagdict[stackfrom][-1])
		bagdict[stackfrom].pop(-1)
	bagdict[stackto] = bagdict[stackto] + list(reversed(temparr))


# instructions
for instruct in instructs:
	instruct = instruct.split(" ")
	stackrange = int(instruct[1])
	stackfrom = int(instruct[3])
	stackto = int(instruct[5])
	move(stackfrom, stackto, stackrange)

for bag in bagdict:
	print(bag[-1], end="")