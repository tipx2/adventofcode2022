with open("testinput.txt") as f:
	lines = f.readlines()

head = [0,0]
tail = [0,0]

tail_poses = []

def move_head_update_tail(xy, dir):
	global tail
	saved = head.copy()
	head[xy] += dir
	# if tail in the 3x3, don't move it
	for z in [-1, 0, 1]:
		for w in [-1, 0, 1]:
			 if [head[0]+z, head[1]+w] == tail:
				 return
	# otherwise, move it to the head's last position
	tail = saved
	if not tail in tail_poses:
		tail_poses.append(tail)

for line in lines:
	# head movement
	if line[0] == "D":
		for x in range(int(line[2])):
			move_head_update_tail(1, -1)
	
	elif line[0] == "U":
		for x in range(int(line[2])):
			move_head_update_tail(1, 1)
			
	elif line[0] == "L":
		for x in range(int(line[2])):
			move_head_update_tail(0, -1)
		
	elif line[0] == "R":
		for x in range(int(line[2])):
			move_head_update_tail(0, 1)

	
print(len(tail_poses)+1)