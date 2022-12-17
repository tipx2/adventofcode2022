with open("13input.txt") as f:
	lines = f.read().split("\n\n")

correct_pair_indexes = []

def compare(left, right):
		breaking = None
		n = 0
		while breaking == None:
			if len(left) == len(right) and len(left) <= n:
				return None
			elif n >= len(right):
				breaking = False
			elif n >= len(left):
				breaking = True
				
			elif not (type(left[n]) == type(right[n])):
				# one's a list and one's a int
				if isinstance(left[n], int) and isinstance(right[n], list):
					breaking = compare([left[n]], right[n])
																										
				elif isinstance(left[n], list) and isinstance(right[n], int):
					breaking = compare(left[n], [right[n]])
				
			elif isinstance(left[n], int) and isinstance(right[n], int):
					# they are both ints
					if left[n] < right[n]:
							breaking = True
					elif left[n] > right[n]:
							breaking = False
					
			elif isinstance(right[n], list) and isinstance(left[n], list):
					# they are both lists
					breaking = compare(left[n], right[n])

			n += 1

		return breaking


for i, pair in enumerate(lines):
		left, right = pair.split("\n")
		left = eval(left)
		right = eval(right)

		
		if compare(left, right):
				correct_pair_indexes.append(i+1)
		# if it's false it just skips to next pair
		# print(i)
print(sum(correct_pair_indexes))