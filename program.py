# Advent Of Code day 01

depth_num = []
prev_number = 0
count_increse = 0

with open('input.txt') as f:
    lines = f.read().splitlines()

    for i in lines:
    	depth_num.append(int(i))

    for i in depth_num:

    	if prev_number < i:
           		count_increse = count_increse + 1
    	prev_number = i

print(count_increse - 1) # settings -1 to make sure it not counts the starting poinr

