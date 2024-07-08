from typing import Optional

from LeetCode.utils import TreeNode
"""
--easy--
https://leetcode.com/problems/merge-two-binary-trees
You are given two binary trees root1 and root2. Combine both trees to make one tree. 
If both trees have the same node.. add their values and their children along

Solution -  Runtime: 95%
            Memory: 42%
"""

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # Here we return the left tree by adding or assigning the right tree counterparts
        if root1 and root2:
            root1.val += root2.val
            if root1.left and root2.left:
                root1.left = self.mergeTrees(root1.left, root2.left)
            if root1.right and root2.right:
                root1.right = self.mergeTrees(root1.right, root2.right)
            if not root1.left and root2.left:
                root1.left = root2.left
            if not root1.right and root2.right:
                root1.right = root2.right
        elif root2:
            # In case there is no root1, we create one by using root2 items and add it to the parent node
            root1 = root2
        return root1




tree1 = TreeNode(1,
                 TreeNode(3,
                          TreeNode(5)
                          ),
                 TreeNode(2,
                          TreeNode(6)
                          )
                 )
tree2 = TreeNode(2,
                 TreeNode(1,
                          None,
                          TreeNode(4)
                          ),
                 TreeNode(3,
                          None,
                          TreeNode(7)
                          )
                 )
tree = Solution().mergeTrees(tree1, tree2)
print(tree)
print(tree.left)
print(tree.right)
print(tree.left.left)
