with open("input4.txt") as f:
	lines = f.readlines()


def part_1():
	total = 0
	for line in lines:
		elf1, elf2 = line.split(",")
		elf2 = elf2.strip()
		# e.g. 3-5, 2-6
		if (int(elf1.split("-")[0]) >= int(elf2.split("-")[0]) and int(elf1.split("-")[1]) <= int(elf2.split("-")[1])) or (int(elf1.split("-")[0]) <= int(elf2.split("-")[0]) and int(elf1.split("-")[1]) >= int(elf2.split("-")[1])):
			# then elf1 is contained within elf2 or then elf2 is contained within elf1
			total += 1
	print(total)

def part_2():
	total = 0
	for line in lines:
		elf1, elf2 = line.split(",")
		elf2 = elf2.strip()

		elf1part1, elf1part2 = elf1.split("-")
		elf2part1, elf2part2 = elf2.split("-")
		
		if set.intersection(set(range(int(elf1part1), int(elf1part2)+1)), set(range(int(elf2part1), int(elf2part2)+1))) != set():
			total += 1
	print(total)

print("part 1:")
part_1()
print("part 2:")
part_2()