1.
def rotate_list(lst):
	# Rotates the list by moving the first element to the end
	if not lst:
		return lst
	return lst[1:] + lst[:1]

my_list = [1,2,3,4,5]
print("Rotated list:", rotate_list(my_list))








