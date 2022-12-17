with open("test13.txt") as f:
	lines = f.read().split("\n\n")

def comparevalues(left, right):
	if not isinstance(left, type(right)):
		# one's a list and one's a int
		if isinstance(left, int) and isinstance(right, list):
			return comparevalues([left], right)
													
		elif isinstance(left, list) and isinstance(right, int):
			return comparevalues(left, [right])
			
	elif isinstance(left, int) and isinstance(right, int):
		# they are both ints (hahaha)
		if left == right:
			return "cont"
		elif left < right:
			return True
		elif left > right:
			return False
			
	elif isinstance(left, list) and isinstance(right, list):
		# they are both lists (hohoho)
		if len(right) == 0:
			return False
		elif len(left) == 0:
			return True
		min_len = min(len(left), len(right))
		return all([comparevalues(left[n], right[n]) for n in range(min_len)])
			
		

correct_pair_indexes = []

for i, line in enumerate(lines):
	left, right = line.split("\n")
	left = eval(left)
	right = eval(right)

	
	min_len = min(len(left), len(right))
	for n in range(min_len):
		g = comparevalues(left[n], right[n])
		if not g:
			# g is false, skip to next pair
			break
		elif g != "cont":
			# if g is true and isn't cont, record it
			correct_pair_indexes.append(i+1)
			break
		
print(sum(correct_pair_indexes))