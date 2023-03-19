


def count_inversions(arr, arr_len = 0):
	arr_len = arr_len or len(arr)

	counter = 0

	def merge_and_count(arr1_start, arr1_end, arr2_start, arr2_end, arr):
		arr1_len = arr1_end - arr1_start + 1
		arr2_len = arr2_end - arr2_start + 1

		arr1 = arr[arr1_start:arr1_end+1]
		arr2 = arr[arr2_start:arr2_end+1]


		i,j = 0,0
		counter = 0

		for k in range(arr1_start,arr2_end+1):
			if i==arr1_len:
				arr[k] = arr2[j]
				j+=1
			elif j==arr2_len:
				arr[k] = arr1[i]
				i+=1
			else:
				is_j_greater = arr2[j]>arr1[i]
				counter+=(arr1_len-i)*(not is_j_greater)
				arr[k] = arr2[j]*(not is_j_greater) + arr1[i]*(is_j_greater)
				i+=is_j_greater
				j+=(not is_j_greater)
		return counter



	def merge_sort(start, end, arr):
			nonlocal counter
			if start==end:
				return
			mid = (end-start)//2
			merge_sort(start, start+mid,arr)
			merge_sort(start+mid+1, end, arr)
			counter += merge_and_count(start,start+mid,start+mid+1, end, arr)

	merge_sort(0,arr_len-1,arr)
	return counter





def main():
	print(count_inversions([1,3,4,2,5,6]))

if __name__ == '__main__':
	main()
