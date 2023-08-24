from datetime import datetime
from typing import Optional

from LeetCode.constants import ListNode
"""
--easy--
https://leetcode.com/problems/reverse-linked-list
Reversing a linked list 

"""

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        This uses recursive approach, however there is a iterative aproach as well

        Solution -  Runtime 61%
                    Memory - 9.5%
        """
        # In case head is None, then return None; Used DeMorgan's law
        if not (head and head.next):
            return head
        n = head.next
        final = self.reverseList(n)
        head.next = None
        n.next = head
        return final


ll = ListNode(6, ListNode(6, ListNode(90, ListNode(45, ListNode(55, ListNode(21))))))
l1 = ListNode(6, ListNode(5))
l2 = ListNode(3)
s_time = datetime.now()
print(Solution().reverseList(l1))
print("The solution took %s "%(datetime.now()-s_time))

