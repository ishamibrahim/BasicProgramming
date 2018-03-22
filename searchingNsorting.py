
import pdb
arr = [3, 97, 63, 55, 32, 56, 99, 22]

#=====================INSERTION SORT====================================

def insertion_sort(unsorted_arr):
	
	len_arr = len(unsorted_arr)

	for out in range(1, len_arr):
		if unsorted_arr[out] < unsorted_arr[out-1]:
			key = unsorted_arr[out]
			inc = out
			while (inc > 0 and key < unsorted_arr[inc -1]):
				unsorted_arr[inc ] = unsorted_arr[inc - 1]
				inc -= 1
			unsorted_arr[inc] = key	
		print unsorted_arr
	print unsorted_arr
	

#=====================SELECTION SORT====================================

def selection_sort(unsorted_arr):
	pivot = 0
	len_arr = len(unsorted_arr)
	
	def swap(index_1, index_2, swap_arr):
		temp = swap_arr[index_1]
		unsorted_arr[index_1] = swap_arr[index_2]
		unsorted_arr[index_2] = temp
	
	for i in range(len_arr-1):
		ex_index = pivot
		ex = None
		for count in range(pivot, len_arr):
			if unsorted_arr[ex_index] > unsorted_arr[count]:
				ex_index = count
				ex = True
		if ex:
			# Swapping
			swap(ex_index, pivot, unsorted_arr)
		pivot += 1
		
	print unsorted_arr


#=====================BINARY SEARCH=====================================
def binary_search(unsorted_arr, item):
	sorted_arr = sorted(unsorted_arr)
	print sorted_arr
	len_arr = len(sorted_arr)
	bisect = len_arr/2
	if item==sorted_arr[bisect]:
		print "Item found at {}".format(bisect+1)
	elif item < sorted_arr[bisect]:
		return binary_search(sorted_arr[:bisect-1], item)
	elif item > sorted_arr[bisect]:
		return binary_search(sorted_arr[bisect:], item)
	

#=====================MERGE SORT========================================
def merge(arr1, arr2):
	sorted_list = []
	while arr1 or arr2:
		if arr1 and arr2:
			if  arr1[0] < arr2[0]:
				sorted_list.append(arr1.pop(0))
			elif arr2[0] < arr1[0]:
				sorted_list.append(arr2.pop(0))
		elif arr1:
			while arr1:
				sorted_list.append(arr1.pop(0))
		else:
			while arr2:
				sorted_list.append(arr2.pop(0))
	return sorted_list

def merge_sort(unsorted_arr):
	def split_arrays(len_unsplit, unsplit_arr):
		median = len_unsplit/2
		
		arr1 = unsplit_arr[: median]
		arr2 = unsplit_arr[median:]
		return arr1, arr2
		
	sorted_arr = []
	len_arr = len(unsorted_arr)
	if len_arr > 1:
		arr1, arr2 = split_arrays(len_arr, unsorted_arr)
		arr1 = merge_sort(arr1)
		arr2 = merge_sort(arr2)
		print arr1, arr2
		sorted_arr = merge(arr1, arr2)
	else:
		return unsorted_arr
	return sorted_arr
		

#=====================QUICK SORT========================================


def quick_sort(unsorted_arr):
	def swap(index_1, index_2, swap_arr):
		temp = swap_arr[index_1]
		unsorted_arr[index_1] = swap_arr[index_2]
		unsorted_arr[index_2] = temp
	len_arr = len(unsorted_arr)
	if len_arr > 1:
		back = -1
		front = 0
		pivot = unsorted_arr[len_arr - 1]
		
		while front < len_arr:
			if unsorted_arr[front] < pivot:
				back += 1
				swap(back, front, unsorted_arr)
			front += 1
	else:
		return unsorted_arr
	back += 1


	left = quick_sort(unsorted_arr[:back])
	right = quick_sort(unsorted_arr[back:len_arr-1])
	return left + [pivot] + right


print quick_sort(arr)
