"""
Find all subsets in a list whose SUM equals given number
"""
import time
from datetime import datetime

SET_OF_NUMS = [30, 12, 15, 18, 13, 5, 10, 7]
LEN_OF_NUMS = len(SET_OF_NUMS)
final_subset_list = []
EXPECTED_SUM = 30


def find_subsets(start: int, subset_list: list, total: int = 0):
    print(subset_list, " ------- ", total)
    if total == EXPECTED_SUM:
        final_subset_list.append("-".join(map(str, subset_list)))
    elif start < LEN_OF_NUMS:
        for i in range(start, LEN_OF_NUMS):
            subset_list.append(SET_OF_NUMS[i])
            total += SET_OF_NUMS[i]
            if total > EXPECTED_SUM:
                if subset_list:
                    print(subset_list, " ------- ", total, " rejected")
                    total -= SET_OF_NUMS[i]
                    subset_list.pop()

            else:
                find_subsets(i+1, subset_list, total)
                total -= SET_OF_NUMS[i]
                subset_list.pop()

# [30, 12, 15, 18, 13, 5, 10, 7]
def find_subsets_2(start: int, subset_list: list):
    if sum(subset_list) == EXPECTED_SUM:
        final_subset_list.append(subset_list[:])
        subset_list.pop()
        return
    for i in range(start, len(SET_OF_NUMS)):
        subset_list.append(SET_OF_NUMS[i])
        if sum(subset_list) > EXPECTED_SUM:
            subset_list.pop()
        else:
            find_subsets_2(i+1, subset_list)
    if subset_list:
        subset_list.pop()





timenow = datetime.now()
find_subsets_2(0, [])
print(final_subset_list)
print(f"total seconds --- {datetime.now() - timenow}")
