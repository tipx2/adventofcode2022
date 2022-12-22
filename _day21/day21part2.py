import sys
from copy import deepcopy

if len(sys.argv) == 2:
    file_t = sys.argv[1]
else:
    file_t = "input21.txt"

with open(file_t) as f:
    monkeys_lines = f.readlines()


# monkeys will be a dictionary with keys that are the names
# a value will look like ["aaaa": [4]]
# an expression will look like ["bbbb":["ahmd", "*", "zczc"]]
# this way instead of typechecking, we can check for expression or value with len()

# while root is an expression:
    # pass 1   
    # go through list to find any monkeys with a value
    # when we hit that, go through all monkeys with expressions and replace the ones with that previous monkey with that previous monkey's value

    # pass 2
    # go through the list to find any monkeys with complete sums
    # do the sum and set that monkey to the value
# print root's output

monkeys = {}
for line in monkeys_lines:
    key, op = line.split(":")
    op = op.strip()
    if len(op) < 4:
        # it's a value
        monkeys[key] = [int(op)]
    else:
        # it's an eqn
        monkeys[key] = op.split(" ")

def replace_monkey(monk, value):
    for m in monkeys.keys():
        if len(monkeys[m]) == 3:
            for x in [0,2]:
                if monkeys[m][x] == monk:
                    monkeys[m][x] = value
                    break

saved_monks = deepcopy(monkeys)

low = 0
high = 5_000_000_000_000

breaking = False
while not breaking:
    monkeys = deepcopy(saved_monks)
    mid = (low + high) //2
    monkeys["humn"] = [mid]
    
    print(mid)
    while len(monkeys["root"]) == 3 and not breaking:
        for monk in monkeys.keys():
            if len(monkeys[monk]) == 1:
                # replace all expressions with this number
                replace_monkey(monk, monkeys[monk][0])
        
        for monk in monkeys.keys():
            if len(monkeys[monk]) == 3:
                if (isinstance(monkeys[monk][0], int) or isinstance(monkeys[monk][0], float)) and (isinstance(monkeys[monk][2], int) or isinstance(monkeys[monk][2], float)):
                    if monk == "root":
                        if monkeys["root"][0] == monkeys["root"][2]:
                            print(mid)
                            breaking = True
                            break
                        else:
                            # they are not equal
                            if monkeys["root"][0] > 122624242469304:
                                low = mid + 1
                            elif monkeys["root"][0] < 122624242469304:
                                high = mid - 1
                    monkeys[monk] = [eval("".join(str(x) for x in monkeys[monk]))]
                        
