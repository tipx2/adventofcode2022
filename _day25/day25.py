import sys

if len(sys.argv) == 2:
    file_t = sys.argv[1]
else:
    file_t = "input25.txt"

with open(file_t) as f:
    lines = f.readlines()

def snafu_to_dec(string):
    total = 0
    for idx, letter in enumerate(reversed(string.strip())):
        if letter == "-":
            multiplier = -1
        elif letter == "=":
            multiplier = -2
        else:
            multiplier = int(letter)
        
        total += (5**idx) * multiplier
    return total

big_total = 0
for line in lines:
    big_total += snafu_to_dec(line)


# 37067035390042 is the total of my list
print(big_total)

s = "=-012"
out = ""
while big_total > 0:
    n = (big_total + 2) % 5
    big_total = (big_total + 2) // 5
    out += s[n]


print("".join(list(reversed(out.strip("0")))))