# Advent Of Code day 01


depth_num = []
prev_number = 0
count_increse = 0

with open('input.txt') as f:
    lines = f.read().splitlines()

    for i in lines:
    	depth_num.append(int(i))

    for i in depth_num:

    	if prev_number == i:
    		print("Same")
    	elif prev_number > i:
    		print("No increse")
    	elif prev_number < i:
    		print("increse")
    		count_increse = count_increse + 1
    	prev_number = i

print(count_increse)

