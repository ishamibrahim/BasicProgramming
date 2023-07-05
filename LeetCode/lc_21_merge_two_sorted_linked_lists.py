# Definition for singly-linked list.
"""
https://leetcode.com/problems/merge-two-sorted-lists/

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Solution    -   51.6% in Runtime
            -   32.4% in Memory

"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        final_list = last_list = None
        node_to_add = None
        while list1 or list2:
            if list1 and list2:
                if list1.val < list2.val:
                    node_to_add = list1
                    list1 = list1.next
                else:
                    node_to_add = list2
                    list2 = list2.next
            elif list1:
                node_to_add = list1
                break
            else:
                node_to_add = list2
                break
            if not final_list:
                final_list = last_list = node_to_add
                node_to_add.next = None
            else:
                last_list.next = node_to_add
                last_list = last_list.next
        if last_list:
            last_list.next = node_to_add
        else:
            final_list = node_to_add

        return final_list


l1 = ListNode(2, ListNode(5, ListNode(8)))
l2 = ListNode(3, ListNode(9))
result = Solution().mergeTwoLists(l1, l2)
while result:
    print(result.val)
    result = result.next







