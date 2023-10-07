"""

Given an array of sorted meeting time intervals of start and end times, determine if a person could attend all meetings

Ex: [(0,10),  (5, 30), (15, 20)] ==> false

"""
from typing import List, Tuple
from LeetCode.constants import Interval


class Solution:
    def can_attend_all_meetins(self, meetings : List[Interval]):
        attend_all = True
        if meetings:
            for i in range(len(meetings) -1):
                if meetings[i].end > meetings[i+1].start:
                    attend_all = False
                    break
        return attend_all


l1 = []
l2 = [Interval(0, 10), Interval(5, 10), Interval(15, 30)]
l3 = [Interval(0,8), Interval(10, 15), Interval(15, 20)]
l4 = [Interval(5, 50)]

print(Solution().can_attend_all_meetins(l2))
