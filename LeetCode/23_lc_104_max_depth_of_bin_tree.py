from typing import Optional

from LeetCode.utils import TreeNode
"""
    https://leetcode.com/problems/maximum-depth-of-binary-tree/
    Given the root of a binary tree, return its maximum depth.
    
    Solution -  Runtime: 96%
                Memory: 13.3%
    
"""

class Solution:
    def find_max_depth(self, node: Optional[TreeNode], level:int) -> int:
        if node.left and node.right:
            return max(self.find_max_depth(node.left, level+1), self.find_max_depth(node.right, level+1))
        if node.left:
            return self.find_max_depth(node.left, level+1)
        if node.right:
            return self.find_max_depth(node.right, level+1)
        return level

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Takes a recursive approach to travel left or right nodes
        if root:
            return self.find_max_depth(root, 1)
        else:
            return 0

tree1 = TreeNode(1,
                 TreeNode(2,
                          TreeNode(4,
                                   TreeNode(8,
                                            TreeNode(9,
                                                     TreeNode(10,
                                                              None,
                                                              TreeNode(11,
                                                                       None,
                                                                       TreeNode(12))))),
                                   TreeNode(13)
                                   ),
                          TreeNode(5)
                          ),
                 TreeNode(3,
                          None,
                          TreeNode(7)
                          )
                 )
print(Solution().maxDepth(tree1))
