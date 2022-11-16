# Advent Of Code day 01

depth_num = []
prev_number = 0
count_inc = 0

with open('input.txt') as f:
    lines = f.read().splitlines()

    for i in lines:
    	depth_num.append(int(i))

    for i in depth_num:
    	if prev_number < i:
            count_inc= count_inc + 1
    	prev_number = i

print(count_inc - 1) # we dont want it to count the first number of the dive.

