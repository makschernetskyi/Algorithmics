


def search(arr,x):

	if len(arr) == 1:
		return [x] == arr

	return search(arr[:len(arr)//2],x) or search(arr[len(arr)//2:],x)



if __name__ == '__main__':

	arr = [1,5,3,-2,6,8,2]

	print(search(arr, 3))