from typing import Optional, List

from LeetCode.utils import TreeNode
from collections import deque
"""
https://leetcode.com/problems/binary-tree-right-side-view
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
Ex: 
Ex Input: root = [3,5,1,6,2,0,8,null,null,7,4]
                       3
                    /     \
                   5        1
                 /   \    /   \
                6    2   0     8
                   /   \
                  7     4
output = [3, 1, 8, 4]

"""



class Solution:
    """
        Solution uses a level order traversal and a dictionary to keep right or left most node in every level of the binary tree
        Runtime: 97%
        Memory: 46%
    """
    def __init__(self):
        self.right_side_view = []
        self.left_side_view = []
        self.level_dict = {}

    def add_node_to_queue(self, node, level):
        deq = self.level_dict.get(level)
        if not deq:
            deq = deque()
            self.level_dict[level] = deq
            self.left_side_view.append(node.val)
        deq.append(node)

    def level_order_traversal_right(self, level):
        deq = self.level_dict[level]
        while deq:
            node = deq.popleft()
            if node.left:
                self.add_node_to_queue(node.left, level+1)
            if node.right:
                self.add_node_to_queue(node.right, level+1)
            if not deq:
                self.right_side_view.append(node.val)


    def level_order_traversal_left(self, level):
        deq = self.level_dict[level]
        while deq:
            node = deq.popleft()
            if node.left:
                self.add_node_to_queue(node.left, level+1)
            if node.right:
                self.add_node_to_queue(node.right, level+1)

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        level = 1
        first_queue = deque()
        first_queue.append(root)
        self.level_dict[level] = first_queue
        if root:
            while True:
                self.level_order_traversal_right(level)
                level += 1
                if not self.level_dict.get(level):
                    break
        return self.right_side_view

    def leftSideView(self, root: Optional[TreeNode]) -> List[int]:
        level = 1
        first_queue = deque()
        first_queue.append(root)
        self.level_dict[level] = first_queue
        if root:
            self.left_side_view.append(root.val)
            while True:
                self.level_order_traversal_left(level)
                level += 1
                if not self.level_dict.get(level):
                    break
        return self.left_side_view

bin_tree =  TreeNode(3,
                    TreeNode(5,
                             TreeNode(6),
                             TreeNode(2,
                                      TreeNode(7),
                                      TreeNode(4)
                                      )
                             ),
                    TreeNode(1,
                             TreeNode(0),
                             TreeNode(8)
                             )
                    )
print(Solution().rightSideView(bin_tree))
print(Solution().leftSideView(bin_tree))
