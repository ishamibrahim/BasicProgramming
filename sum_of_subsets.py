
SET_OF_NUMS = [5, 10, 12, 13, 15, 18]
sum_nums = sum(SET_OF_NUMS)
LEN_OF_NUMS = len(SET_OF_NUMS)
final_subset_list = []
FINAL_SUM = 28


def find_subsets(start: int, subset_list: list, total: int):
    if total == FINAL_SUM:
        final_subset_list.append("-".join(map(lambda x: str(x), subset_list)))
    if start < LEN_OF_NUMS:
        for i in range(start, LEN_OF_NUMS):
            subset_list.append(SET_OF_NUMS[i])
            total += SET_OF_NUMS[i]
            if total > FINAL_SUM:
                if subset_list:
                    total -= SET_OF_NUMS[i]
                    subset_list.pop()
            else:
                find_subsets(i+1, subset_list, total)
                total -= SET_OF_NUMS[i]
                subset_list.pop()


find_subsets(0, [], 0)
print(final_subset_list)
