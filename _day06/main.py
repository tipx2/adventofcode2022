with open("i6nput6.txt") as f:
    lines = f.read()

lookahead = 14

for x in range(len(lines)):
    print(lines[x:x+lookahead])
    if len(list(set(lines[x:x+lookahead]))) == lookahead:
        print(x+lookahead)
        break