from datetime import datetime
from typing import Optional
from .constants import ListNode

"""
--easy--
https://leetcode.com/problems/middle-of-the-linked-list/

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

"""


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Uses the same hare and tortoise approach
        Solution -  Runtime 80.2%
                    Memory 21.4%
        """
        front = back = head
        while front and front.next :
            front = front.next.next
            back = back.next
        return back


ll = ListNode(6, ListNode(6, ListNode(90, ListNode(45, ListNode(55, ListNode(21))))))

s_time = datetime.now()
print(Solution().middleNode(ll))
print("The solution took %s "%(datetime.now()-s_time))

