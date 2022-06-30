import pdb

arr = [3, 97, 63, 55, 32, 56, 99, 22]


# =====================INSERTION SORT====================================

def insertion_sort(unsorted_arr):
    len_arr = len(unsorted_arr)

    for out in range(1, len_arr):
        if unsorted_arr[out] < unsorted_arr[out - 1]:
            key = unsorted_arr[out]
            inc = out
            while (inc > 0 and key < unsorted_arr[inc - 1]):
                unsorted_arr[inc] = unsorted_arr[inc - 1]
                inc -= 1
            unsorted_arr[inc] = key
        print(unsorted_arr)
    print(unsorted_arr)


# =====================SELECTION SORT====================================

def selection_sort(unsorted_arr):
    pivot = 0
    len_arr = len(unsorted_arr)

    def swap(index_1, index_2, swap_arr):
        temp = swap_arr[index_1]
        unsorted_arr[index_1] = swap_arr[index_2]
        unsorted_arr[index_2] = temp

    for i in range(len_arr - 1):
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

    print (unsorted_arr)


# =====================BINARY SEARCH=====================================
def binary_search_index(sorted_arr, first, last, item):
    bisect = int((first+last) / 2)
    if first >= last:
        print("Item not found")
    elif item == sorted_arr[bisect]:
        print("Item found at {}".format(bisect))
    elif item < sorted_arr[bisect]:
        return binary_search_index(sorted_arr, first, bisect-1, item)
    elif item > sorted_arr[bisect]:
        return binary_search_index(sorted_arr, bisect+1, last, item)

def binary_search(unsorted_arr, item):
    sorted_arr = sorted(unsorted_arr)
    print(sorted_arr)
    binary_search_index(sorted_arr, 0, len(sorted_arr)-1, item)


# =====================MERGE SORT========================================
def merge(arr1, arr2):
    sorted_list = []
    while arr1 or arr2:
        if arr1 and arr2:
            if arr1[0] < arr2[0]:
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
        median = len_unsplit / 2

        arr1 = unsplit_arr[: median]
        arr2 = unsplit_arr[median:]
        return arr1, arr2

    sorted_arr = []
    len_arr = len(unsorted_arr)
    if len_arr > 1:
        arr1, arr2 = split_arrays(len_arr, unsorted_arr)
        arr1 = merge_sort(arr1)
        arr2 = merge_sort(arr2)
        print(arr1, arr2)
        sorted_arr = merge(arr1, arr2)
    else:
        return unsorted_arr
    return sorted_arr


# =====================QUICK SORT========================================


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
    right = quick_sort(unsorted_arr[back:len_arr - 1])
    return left + [pivot] + right

# print(quick_sort([-2, 3, -1, 5, 4, 3, 0]))


def swap(ind1, ind2, arr):
    temp = arr[ind1]
    arr[ind1] = arr[ind2]
    arr[ind2] = temp

def quick_sort_2(low, high, unsorted_arr):
    if low < high:
        f = low
        b = low-1
        piv = unsorted_arr[high]
        while f <= high:
            if unsorted_arr[f] < piv:
                b += 1
                swap(b, f, unsorted_arr)
            f += 1
        b += 1
        swap(b, high, unsorted_arr)
        quick_sort_2(low, b-1, unsorted_arr)
        quick_sort_2(b+1, high, unsorted_arr)

################ HEAP SORT  ####################
def create_min_heap(unsorted_arr):
    min_heap = [-1000000, unsorted_arr[0]]
    for i in unsorted_arr[1:]:
        min_heap.append(i)
        last_sorted_elem_index = len(min_heap) -1
        last_sorted_parent_index = int(last_sorted_elem_index/2)
        while last_sorted_parent_index > 0 :
            if min_heap[last_sorted_elem_index] < min_heap[last_sorted_parent_index]:
                swap(last_sorted_parent_index, last_sorted_elem_index, min_heap)
            last_sorted_elem_index = last_sorted_parent_index
            last_sorted_parent_index = int(last_sorted_elem_index/2)
    return min_heap


def heapify(min_heap):
    # Removing first element
    pop_index = len(min_heap) - 1
    last_elem = min_heap.pop(pop_index)
    if len(min_heap) > 1:
        min_heap[1] = last_elem
        elem_index = 1

        if len(min_heap) > elem_index*2 or len(min_heap) > elem_index*2+1:
            if len(min_heap) == elem_index * 2 + 1:
                first_child_index = elem_index * 2
            else:
                first_child_index = elem_index*2 if min_heap[elem_index*2] < min_heap[elem_index*2+1] else elem_index*2+1
            while first_child_index < len(min_heap)-1:
                if min_heap[elem_index] > min_heap[first_child_index]:
                    swap(elem_index, first_child_index, min_heap)
                elem_index = first_child_index
                first_child_index = elem_index * 2


def heap_sort(unsorted_arr):
    min_heap = create_min_heap(unsorted_arr)
    print(min_heap)
    sorted_arr = []
    while len(min_heap) > 1:
        sorted_arr.append(min_heap[1])
        heapify(min_heap)

    return sorted_arr

new_arr = [8, 3, -1, 5, 4, 3, 0]

print(heap_sort(new_arr))


