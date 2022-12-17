with open("test11.txt") as f:
	lines = f.read().split("\n\n")

class monkey:
	
	def __init__(self, i, op, cond, t, f):
		self.items = i.copy() # list, i.e. [79, 60, 97]
		self.operation = op # string, i.e. "old + 3" which can be sub'd and eval'd
		self.condition = cond # int, i.e. 17 which can be % == 0'd
		self.truethrow = t # int, i.e. 5
		self.falsethrow = f # int, i.e. 7

	def __repr__(self):
		return str(self.items)
	
	def turn(self, monkeysarr, monkeysinspectcount):
		while self.items != []:
			item = self.items[0]
			# add to inspection count
			monkeysinspectcount[monkeysarr.index(self)] += 1
			# perform operation
			inspect = eval(self.operation.replace("old", str(item)))
			# check
			if inspect % self.condition == 0:
				# throw true
				monkeysarr[self.truethrow].receive(inspect)
			else:
				# throw false
				monkeysarr[self.falsethrow].receive(inspect)
			self.items.remove(item)
			
			
	def receive(self, item):
		self.items.append(item)

monkeysarr = []
# populate monkey array
for line in lines:
	line = line.split("\n")
	i = [int(x) for x in line[1].split(": ")[1:][0].split(",")]
	op = line[2].split("= ")[1]
	#eval(op.replace("old", "79")))
	cond = int(line[3].split("by ")[1])
	t = int(line[4].split("monkey ")[1])
	f = int(line[5].split("monkey ")[1])
	monkeysarr.append(monkey(i,op,cond,t,f))


monkeysinspectcount = [0 for x in range(8)]
for x in range(10000):
	for monkey in monkeysarr:
		monkey.turn(monkeysarr, monkeysinspectcount)
	print(x)

highest, second = sorted(monkeysinspectcount)[-1], sorted(monkeysinspectcount)[-2]
print(highest * second)
