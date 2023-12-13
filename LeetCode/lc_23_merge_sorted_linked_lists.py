"""
https://leetcode.com/problems/merge-k-sorted-lists/
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Solution    -   11.6% in Runtime
            -   32.4% in Memory
"""
from typing import Optional, List
from utils import ListNode

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
        final_list = None
        if lists:
            final_list = lists[0]
            for i in range(1, len(lists)):
                final_list = self.merge(final_list, lists[i])
        return final_list



l1 = ListNode(2, ListNode(5, ListNode(8)))
l2 = ListNode(3, ListNode(9))
l3 = ListNode(6, ListNode(6, ListNode(90)))
result = Solution().mergeKLists([l1, l2, l3])
print(result)
