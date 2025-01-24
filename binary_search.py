def bisection_iter(n, arr):
	start = 0
	stop = len(arr)-1
	while start <= stop:
		mid = (start + stop)//2
		if n == arr[mid]:
			return f"{n} found at index: {mid}"
		elif n > arr[mid]:
			start = mid +1
		else:
			stop = mid -1 
	return f"{n} not found in list"

def create_list(max_val):
	arr = []
	for num in range(12, max_val+1):
		arr.append(num)
	return arr.append(num)
