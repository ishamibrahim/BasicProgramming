"""
--hard--
https://leetcode.com/problems/merge-k-sorted-lists/
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.


"""
from functools import reduce
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
        """
        Solution    -   11.6% in Runtime
                    -   32.4% in Memory
        """
        final_list = None
        if lists:
            final_list = lists[0]
            for i in range(1, len(lists)):
                final_list = self.merge(final_list, lists[i])
        return final_list

####################################### Solution 2 #################################3
    def get_minimal_index(self, list_dict):
        key = reduce(lambda a, b: a if list_dict[a].val < list_dict[b].val else b, list_dict.keys())
        return key

    def mergeKLists2(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        list_dict = {i: lists[i] for i in range(len(lists)) if lists[i]}
        final_result = next_node = ListNode(None, None)
        if len(lists) == 1:
            final_result = lists[0]
            return final_result
        elif not lists:
            return None
        else:
            while True:
                if len(list_dict)>1:
                    min_index = self.get_minimal_index(list_dict)
                    next_node.next= list_dict[min_index]
                    next_node = next_node.next
                    list_dict[min_index] = list_dict[min_index].next
                    next_node.next = None
                    if not list_dict[min_index] :
                        del list_dict[min_index]
                elif len(list_dict) == 1:
                    index_key = next(iter(list_dict))
                    next_node.next = list_dict[index_key]
                    del list_dict[index_key]
                else:
                    break
        return final_result.next



l1 = ListNode(2, ListNode(5, ListNode(8)))
l2 = ListNode(3, ListNode(9))
l3 = ListNode(6, ListNode(6, ListNode(90)))

result = Solution().mergeKLists2([None, None])
print(result)




