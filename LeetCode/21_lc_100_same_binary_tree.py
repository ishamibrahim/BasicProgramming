from typing import Optional

from LeetCode.utils import TreeNode
"""
    https://leetcode.com/problems/same-tree
    Given the roots of two binary trees p and q, write a function to check if they are the same or not.
    Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
    
    Solution -  Runtime : 80%
                Memory  : 92%
    
"""

class Solution:

    def check_tree_recursively(self, node1, node2) -> bool:
        if node1.val == node2.val:
            left_tree_same = right_tree_same = False
            if node1.left and node2.left:
                left_tree_same = self.check_tree_recursively(node1.left, node2.left)
                if not left_tree_same:
                    return False
            elif not (node1.left or node2.left):
                left_tree_same = True
            if node1.right and node2.right:
                right_tree_same = self.check_tree_recursively(node1.right, node2.right)
                if not right_tree_same:
                    return False
            elif not (node1.right or node2.right):
                right_tree_same = True

            if left_tree_same and right_tree_same:
                return True
            else:
                return False
        else:
            return False

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        This is a recursive solution compares the left node and the same right node of both graphs.

        """
        if p and q:
            return self.check_tree_recursively(p, q)
        elif not (p or q):
            return True
        else:
            return False


tree1 = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(8)), TreeNode(5)), TreeNode(3, None, TreeNode(7)))
tree2 = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(8)), TreeNode(5)), TreeNode(3, None, TreeNode(7)))


print(Solution().isSameTree(tree1,tree2))
