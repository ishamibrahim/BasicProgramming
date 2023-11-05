from datetime import datetime
from typing import Optional

from LeetCode.utils import ListNode
"""
--easy--
https://leetcode.com/problems/palindrome-linked-list/

Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

This solution is from neetcode video. The solution I thought of was storing values in an array and iterating from both ends

"""

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        Solution -  Runtime: 92%
                    Memory: 75.6%
        """

        result = True
        front = back = head
        # using hare and tortoise method we reach the middle of the linkedlist
        while front and front.next:
            front = front.next.next
            back = back.next
        mid = back

        # Reverse the linkedlist from the middle iteratively (cal also use recursion)
        temp = mid
        nex = mid.next
        temp.next = None

        while nex:
            mid = nex
            nex = mid.next
            mid.next = temp
            temp = mid

        # Check if two linked lists are equal
        while mid:
            if mid.val != head.val:
                result = False
                break
            mid, head = mid.next, head.next

        return result





ll = ListNode(6, ListNode(6, ListNode(90, ListNode(45, ListNode(55, ListNode(21))))))
l1 = ListNode(6, ListNode(5, ListNode(5, ListNode(6))))
l2 = ListNode(3, ListNode(4))
s_time = datetime.now()
print(Solution().isPalindrome(l2))
print("The solution took %s "%(datetime.now()-s_time))


