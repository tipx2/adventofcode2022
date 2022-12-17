with open("input10.txt") as f:
	lines = f.readlines()

xvalues = {}
x = 1
cycles = 0

for line in lines:
	cycles += 1
	xvalues[cycles] = x
	if line.split(" ")[0] == "addx":
		cycles += 1
		xvalues[cycles] = x
		x += int(line.split(" ")[1])
 # now we have a dictionary of key: cycles, value: x at that cycle

# part 1
print(sum(xvalues[x] * x for x in [20,60,100,140,180,220]))

# part 2
screen = ""
for x in xvalues:
	if (x % 40) == 0:
		screen += "\n"
	elif (x%40)-1 in [xvalues[x], xvalues[x]-1, xvalues[x]+1]:
		screen += "█"
	else:
		screen += "░"
print(screen)