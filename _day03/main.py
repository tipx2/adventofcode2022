with open("input3.txt") as f:
    lines = f.readlines()

def part_1():
    total = 0
    for line in lines:
        compart1 = line[0:(len(line)//2)]
        compart2 = line[(len(line)//2):]
        
        ruckarray = [compart1,compart2]
        common_letter = set.intersection(*map(set,ruckarray))
        common_letter = common_letter.pop()
        
        if common_letter.isupper():
            total += (ord(common_letter)-38)
        elif common_letter.islower():
            total += (ord(common_letter)-96)
    print(total)

def part_2():
    total = 0
    for x in range(0,len(lines)-1, 3):
        first = lines[x].strip()
        second = lines[x+1].strip()
        third = lines[x+2].strip()
        
        ruckarray = [first, second, third]
        
        common_letter = set.intersection(*map(set,ruckarray))
        common_letter = common_letter.pop()
        
        if common_letter.isupper():
            total += (ord(common_letter)-38)
        elif common_letter.islower():
            total += (ord(common_letter)-96)
        
    print(total)

print("part 1:")
part_1()
print("part 2:")
part_2()