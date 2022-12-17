import timeit
mysetup = '''
with open("13input.txt") as f:
	lines = f.read().split("\n\n")
'''
mycode = '''
	def compare(left, right):
			breaking = None
			n = 0
			while breaking == None:
				if left == right:
					return None
				
				elif len(left) == len(right) and len(left) <= n:
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
	
	bigarr = []
	for pair in lines:
		left, right = pair.split("\n")
		bigarr.append(eval(left))
		bigarr.append(eval(right))
	
	def sort_big(arr):
		for i in range(len(arr)-1):
			for j in range(len(arr)-i-1):
				if compare(arr[j+1], arr[j]):
					arr[j], arr[j+1] = arr[j+1], arr[j]
		return arr
	# sort bigarr
	bigarr = sort_big(bigarr)
	# compare returns true if left is smaller
	print((bigarr.index([[2]])+1) * (bigarr.index([[6]])+1))
'''
print (timeit.timeit(setup = mysetup,
                     stmt = mycode,
                     number = 10000))