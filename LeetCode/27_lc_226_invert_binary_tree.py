from typing import Optional

from LeetCode.utils import TreeNode
"""
https://leetcode.com/problems/invert-binary-tree
Given the root of a binary tree, invert the tree, and return its root.

Solution -  Runtime: 82%
            Memory: 35.4%

"""

class Solution:
    def invert(self, root: Optional[TreeNode]):
        if root:
            root.left, root.right = root.right, root.left
            if root.left:
                self.invert(root.left)
            if root.right:
                self.invert(root.right)

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.invert(root)
        return root


tree1 = TreeNode(1,
                 TreeNode(3,
                          TreeNode(5)),
                 TreeNode(2)
                 )
Solution().invertTree(tree1)

print(tree1.left)
print(tree1.right)





