from typing import Optional

from LeetCode.constants import TreeNode
"""
    https://leetcode.com/problems/path-sum
    Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path 
    such that adding up all the values along the path equals targetSum.
    
    Solution -  Runtime: 93%
                Memory : 9.8%
"""


class Solution:
    def has_sum_in_node(self, node, target, current_sum):
        if node:
            current_sum += node.val
            if current_sum == target:
                if not (node.left or node.right):
                    return True
            if node.left and node.right:
                return self.has_sum_in_node(node.left, target, current_sum) or self.has_sum_in_node(node.right, target, current_sum)
            if node.left:
                return self.has_sum_in_node(node.left, target, current_sum)
            if node.right:
                return self.has_sum_in_node(node.right, target, current_sum)
            return False
        else:
            return False

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.has_sum_in_node(root, targetSum, 0)

tree1 = TreeNode(1,
                 TreeNode(2,
                          TreeNode(4,
                                   TreeNode(8)
                                   ),
                          TreeNode(5)
                          ),
                 TreeNode(3,
                          None,
                          TreeNode(7)
                          )
                 )
tree2 = TreeNode(-2,
                 None,
                 TreeNode(-3))
print(Solution().hasPathSum(tree2, -5))
