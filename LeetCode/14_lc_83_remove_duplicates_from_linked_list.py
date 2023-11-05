from LeetCode.utils import ListNode
from typing import Optional
"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Solution -  Runtime: 97.7%
            Memory: 44.5%

"""


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        back = ListNode(-999)
        front  = head
        while front:
            if front.val == back.val:
                back.next = front.next
            else:
                back = front
            front = front.next
        return head


ll = ListNode(6, ListNode(6, ListNode(20, ListNode(45, ListNode(55, ListNode(55))))))
l2 = ListNode(-21, ListNode(6, ListNode(20, ListNode(20, ListNode(55, ListNode(55))))))


print(Solution().deleteDuplicates(l2))

