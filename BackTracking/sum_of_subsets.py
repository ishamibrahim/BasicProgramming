"""
Find all subsets in a list whose SUM equals given number
"""
SET_OF_NUMS = [30, 12, 15, 18, 13, 5, 10]
LEN_OF_NUMS = len(SET_OF_NUMS)
final_subset_list = []
FINAL_SUM = 30


def find_subsets(start: int, subset_list: list, total: int):
    print(subset_list, " ------- ", total)
    if total == FINAL_SUM:
        final_subset_list.append("-".join(map(lambda x: str(x), subset_list)))
    elif start < LEN_OF_NUMS:
        for i in range(start, LEN_OF_NUMS):
            subset_list.append(SET_OF_NUMS[i])
            total += SET_OF_NUMS[i]
            if total > FINAL_SUM:
                if subset_list:
                    print(subset_list, " ------- ", total, " rejected")
                    total -= SET_OF_NUMS[i]
                    subset_list.pop()

            else:
                find_subsets(i+1, subset_list, total)
                total -= SET_OF_NUMS[i]
                subset_list.pop()


find_subsets(0, [], 0)
print(final_subset_list)
