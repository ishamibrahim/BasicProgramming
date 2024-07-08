from typing import List
"""
    --medium--
    Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
    You must write an algorithm that runs in O(n) time.
    Ex: nums = [100,4,200,1,3,2] --> 4 (Since the longest consecutive elements are 1 to 4)
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        This solution contains the sort method inbuilt
        """
        sorted_list = sorted(list(set(nums)))
        count = 0
        max_count = 0
        if sorted_list:
            previous_num = sorted_list[0] - 1
            for num in sorted_list:
                if num == previous_num+1:
                    count += 1
                else:

                    count = 1
                previous_num = num
                max_count = max(count, max_count)
        return max_count

    def longestConsecutive2(self, nums: List[int]) -> int:
        """
        This solution doesn't need to sort
        dict_ value states : 1 ==> not marked 2 ==> marked

        Solution: Runtime: 93%
                 Memory: 6%
        """
        nums_dict = {x: 1 for x in nums}
        num_set = set(nums)
        max_count = 0
        if num_set:
            for num in num_set:
                if not nums_dict.get(num - 1, False) and nums_dict[num] == 1:
                    nums_dict[num] = 2
                    count = 1
                    iterator = num
                    while True:
                        iterator = iterator +1
                        if nums_dict.get(iterator, False):
                            count += 1
                            nums_dict[iterator] = 2
                        else:

                            max_count = max(max_count, count)
                            break
        return max_count






print(Solution().longestConsecutive2([100,4,200,1,3,2]))




