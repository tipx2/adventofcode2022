# A - X - Rock
# B - Y - Paper
# C - Z - Scissors

with open("input1.txt", "r") as f:
	lines = f.read().split("\n")

scoreDict = {"X":1, "Y":2, "Z":3}
winDict = {"X": "C", "Y": "A", "Z": "B"}
drawDict = {"X": "A", "Y": "B", "Z":"C"}
loseDict = {"X":"B", "Y":"C", "Z":"A"}

winDict2 = {winDict[x]:x for x in winDict}
loseDict2 = {loseDict[x]:x for x in loseDict}
drawDict2 = {drawDict[x]:x for x in drawDict}

bigTotal = 0
for line in lines:
	line = line.split(" ")
	result = line[1]
	oppChoice = line[0]
	if result == "X":
		# need to lose
		meChoice = loseDict2[oppChoice]
	elif result == "Y":
		# need to draw
		meChoice = drawDict2[oppChoice]
	elif result == "Z":
		# need to win
		meChoice = winDict2[oppChoice]
	
	if winDict[meChoice] == oppChoice:
		bigTotal += 6
	elif drawDict[meChoice] == oppChoice:
		bigTotal += 3

	bigTotal += scoreDict[meChoice]

print(bigTotal)
	