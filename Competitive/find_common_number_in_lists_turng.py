"""

Given a set of lists containing integers in a sorted order find the least common number in all the lists
ex: req = [[2,4,6,8], [2,3,4,6, 8], [5,6,8,10], [1, 4, 6, 8]]
Result = 6
If no common numbers are found return -1

"""
from typing import List


def find_least_common_number(nums: List[List[int]]):
    first_list = nums[0]
    first_index = 0
    index_dict = {i:0 for i in range(1, len(nums))}
    while first_index < len(first_list):
        common_found = True
        for ind in range(1, len(nums)):
            if nums[ind][index_dict[ind]] < first_list[first_index]:
                while nums[ind][index_dict[ind]] < first_list[first_index] and index_dict[ind] < len(nums[ind])-1:
                    index_dict[ind] += 1
            if nums[ind][index_dict[ind]] != first_list[first_index]:
                common_found = False
        if common_found:
             break
        first_index += 1
    return first_list[first_index]



if __name__ == "__main__":
    req = [[2,4,5, 6,8], [2,3,5, 8], [5,6,8,10], [1, 4, 5, 6, 8]]
    print(find_least_common_number(req))
