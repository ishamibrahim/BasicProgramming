from typing import Optional
from LeetCode.utils import TreeNode

"""
--easy--
https://leetcode.com/problems/diameter-of-binary-tree/

Given the root of a binary tree, return the length of the diameter of the tree.
Solution -  Runtime: 67%
            Memory: 80%
"""

class Solution:
    max_diameter = 0

    def find_max_depth(self, node: Optional[TreeNode]) -> int:
        if node.left and node.right:
            left_depth = self.find_max_depth(node.left)
            right_depth = self.find_max_depth(node.right)
            self.max_diameter = max(self.max_diameter, left_depth + right_depth + 2)
            return max(left_depth+1, right_depth+1)
        if node.left:
            left_depth = self.find_max_depth(node.left)

            self.max_diameter = max(self.max_diameter, left_depth+1)
            return left_depth+1
        if node.right:
            right_depth = self.find_max_depth(node.right)
            self.max_diameter = max(self.max_diameter, right_depth+1)
            return right_depth+1
        return 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        The solution uses the depth of left and right of every node to store in a variable called max
        """
        self.find_max_depth(root)
        return self.max_diameter

tree1 = TreeNode(1,
                 TreeNode(2,
                          TreeNode(4,
                                   TreeNode(8,
                                            TreeNode(9))
                                   ),
                          TreeNode(5,
                                   None,
                                   TreeNode(6,
                                            None,
                                            TreeNode(7,
                                                     None,
                                                     TreeNode(10)
                                                     )
                                            )
                                   )
                          ),
                 TreeNode(3,
                          None,
                          TreeNode(7)
                          )
                 )
tree2 = TreeNode(1,
                 TreeNode(2,
                          TreeNode(4),
                          TreeNode(5)),
                 TreeNode(3))
print(Solution().diameterOfBinaryTree(tree1))
