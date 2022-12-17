with open("input14.txt") as f:
	lines = f.readlines()

sand_spawn = (500, 0)

class RockPath:
	def __init__(self, line):
		self.coords = [(int(x.split(",")[0]), int(x.split(",")[1])) for x in line.split(" -> ")]

	def build_path(self):
		fill_this = []
		# build to next coord
		for i in range(len(self.coords)-1):
			
			if self.coords[i+1][0] == self.coords[i][0]:
				# the first values are the same
				if self.coords[i][1] > self.coords[i+1][1]:
					step = -1
				else:
					step = 1
				
				fill_this += [(self.coords[i][0], x) for x in range(self.coords[i][1], self.coords[i+1][1]+step, step)]
				
			elif self.coords[i+1][1] == self.coords[i][1]:
				# the second values are the same
				if self.coords[i][0] > self.coords[i+1][0]:
					step = -1
				else:
					step = 1
				
				fill_this += [(x, self.coords[i][1]) for x in range(self.coords[i][0], self.coords[i+1][0]+step, step)]
		return fill_this

rockarr = []
for line in lines:
	rockarr += RockPath(line).build_path()

lowest = sorted(rockarr, key=lambda item: item[1])[-1][1]
# aryeh says "SET! SET!!!"
rockarr = set(rockarr)
sandarr = set()


while True: # spooky
	new_sand = sand_spawn
	# check under
	while True:
		under = (new_sand[0], new_sand[1]+1)
		if under in rockarr or under in sandarr:
			# there's a rock beneath
			left = (under[0]-1, under[1])
			right = (under[0]+1, under[1])
			if not left in rockarr and not left in sandarr:
				new_sand = left
			elif not right in rockarr and not right in sandarr:
				new_sand = right
			else:
				sandarr.add(new_sand)
				break
		else:
			new_sand = under
			if new_sand[1] > lowest:
				break

print(len(sandarr))

# sand
# is tentative space in the rock array?
#  - yes -> check left -> right -> stay
#  - no -> move sand down

# rock
# rockpath class has a function that fills the array with the coordinates covered by each range