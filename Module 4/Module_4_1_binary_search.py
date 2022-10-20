my_list = [1,2,3,4,5,7,8,12]
my_list2 = [2,4,6,8,10,12,14]

def binary_search(list,item):
	low = 0
	high = len(list)-1

	while low <= high:
		mid = (low + high)//2
		guess = list[mid]
		if guess == item:
			return mid
		if guess > item:
			high = mid // 2 
		else:
			low = mid + 1
	return None

print(binary_search(my_list, 3))
print(binary_search(my_list2, 3))
