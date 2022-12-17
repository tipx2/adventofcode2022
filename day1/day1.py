with open("input.txt", "r") as f:
	lines = f.readlines()

total = 0
calorray = []
for line in lines:
	if line != '\n':
		total += int(line)
	else:
		calorray.append(total)
		total = 0

print(sum(sorted(calorray)[-3:]))
