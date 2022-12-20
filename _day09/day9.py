from matplotlib import pyplot
from copy import deepcopy
with open("input9.txt") as f:
    lines = f.readlines()

saved_knotsarrs = []

tail_posarr = []
class knot:
	def __init__(self, num):
		self.number = num
		self.pos = [0,0]

	def __repr__(self):
		return str(self.pos.copy())

	def look_at_knot_and_move(self, knot):
		# x, y
		move = [0,0]

		for z in [-1, 0, 1]:
			for w in [-1, 0, 1]:
				 if [knot.pos[0]+z, knot.pos[1]+w] == self.pos:
					 return
		
		if knot.pos[0] > self.pos[0]:
			# we are 2 to the left
			move[0] = 1
		elif knot.pos[0] < self.pos[0]:
				# we are 2 to the right
			move[0] = -1
		
		if knot.pos[1] > self.pos[1]:
			# we are 2 to the down
			move[1] = 1
			
		elif knot.pos[1] < self.pos[1]:
				# we are 2 to the up
			move[1] = -1

		# make a move, make-a make-a move
		self.pos[0] += move[0]
		self.pos[1] += move[1]

		if self.number == 9:
			tail_posarr.append(self.pos.copy())
		

	def head_move(self, xy, dir):
		# xy is 0 or 1 for x and y, and dir is 1 or -1 for neg or pos
		self.pos[xy] += dir

knotsarr = [knot(x) for x in range(10)]

for line in lines:
	xy = 0
	dir = 0
	if line[0] == "U":
		xy = 1
		dir = 1
	elif line[0] == "D":
		xy = 1
		dir = -1
	elif line[0] == "L":
		xy = 0
		dir = -1
	elif line[0] == "R":
		xy = 0
		dir = 1
	
	for z in range(int(line.split(" ")[-1])):
		knotsarr[0].head_move(xy, dir)
		for x in range(len(knotsarr)):
			if x == 0:
				continue
			knotsarr[x].look_at_knot_and_move(knotsarr[x-1])

		saved_knotsarrs.append(deepcopy(knotsarr))
			
#total = 0
#found = []
#for n in tail_posarr:
#	if n not in found:
#		total += 1
#		found.append(n)
#print(total+1)


lims = 200
print("starting plotting process")
pyplot.xlim([-lims, lims])
pyplot.ylim([-lims, lims])
total = 0
for i, k in enumerate(saved_knotsarrs):
    if i % 200 == 0:
        for x in k:
            pyplot.plot(x.pos[0], x.pos[1], markersize=1, color="black")
        pyplot.savefig("images/plot" + str(i) + ".png")
        pyplot.clf()
        pyplot.xlim([-lims, lims])
        pyplot.ylim([-lims, lims])
print(total)