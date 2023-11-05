from typing import Optional

from LeetCode.utils import ListNode
"""
--easy--
https://leetcode.com/problems/remove-linked-list-elements
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

Solution -  Runtime: 86.1%
            Memory: 89.7%
"""
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        front = head
        back = None

        while front:
            if front.val == val:
                if back:
                    back.next = front.next
                else:
                    head = front = front.next
                    continue
            else:
                back = front
            front = front.next

        return head


ll = ListNode(60, ListNode(6, ListNode(90, ListNode(45, ListNode(55, ListNode(6))))))
l2 = ListNode(1, ListNode(6, ListNode(6, ListNode(1))))
print(Solution().removeElements(ll, 6))

