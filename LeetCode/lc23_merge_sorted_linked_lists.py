"""
https://leetcode.com/problems/merge-k-sorted-lists/
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Solution    -   11.6% in Runtime
            -   32.4% in Memory
"""
from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def merge(self, list1, list2):
        llist = ListNode()
        pointer = llist
        while list1 or list2:
            if list1 and list2:
                if list1.val < list2.val:
                    pointer.next = list1
                    list1 = list1.next
                else:
                    pointer.next = list2
                    list2 = list2.next
            elif list1:
                pointer.next = list1
                break
            else:
                pointer.next = list2
                break
            pointer = pointer.next
        return llist.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        llist = None
        if lists:
            llist = lists[0]
            for i in range(1, len(lists)):
                llist = self.merge(llist, lists[i])
        return llist



l1 = ListNode(2, ListNode(5, ListNode(8)))
l2 = ListNode(3, ListNode(9))
l3 = ListNode(6, ListNode(6, ListNode(90)))
result = Solution().mergeKLists([l1, l2, l3])
while result:
    print(result.val)
    result = result.next
