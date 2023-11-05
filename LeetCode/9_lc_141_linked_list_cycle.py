"""
--easy--
https://leetcode.com/problems/linked-list-cycle/

Given head, the head of a linked list, determine if the linked list has a cycle in it.
"""
from typing import Optional
from datetime import datetime
from .utils import ListNode

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        This solution uses a dict to keep track of all the nodes visited.
        Solution -  Runtime 29.5%
                    Memory 14.8%
        """
        is_cyclic = False
        # Using dictionary since access is faster, a list would have been slower since a search would need to loop in it everytime
        nodes = dict()
        while head and head.next:
            if head in nodes:
                is_cyclic = True
                break
            nodes[head] = 1
            head = head.next
        return is_cyclic

    def neetcode(self, head: Optional[ListNode]) -> bool:
        """
        This uses the rabbit and tortoise method, the rabbit moves double the speed of tortoiase.
        A classic way to find out loops in linked list.

        Solution -  Runtime 91.7%
                 -  Memory 72.5%
        """
        is_cylic = False
        hare = head
        tortoise = head
        while hare and hare.next:
            hare = hare.next.next
            tortoise = tortoise.next
            if hare == tortoise:
                is_cylic = True
                break
        return is_cylic


l1 = ListNode(5)
ll = ListNode(6, ListNode(6, ListNode(90, ListNode(45, ListNode(55, ListNode(21, l1))))))
l1.next = ll.next

s_time = datetime.now()
print(Solution().hasCycle(ll))
print("The solution took %s "%(datetime.now()-s_time))
