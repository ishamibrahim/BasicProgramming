from typing import Optional
from LeetCode.constants import TreeNode
"""
    https://leetcode.com/problems/subtree-of-another-tree
    Given the roots of two binary trees root and subRoot, 
    return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
    
    Solution -  Runtime: 87%
                Memory:  57%
"""

class Solution:
    def is_identical_tree(self, tree1: Optional[TreeNode], tree2: Optional[TreeNode]) -> bool:
        if not (tree1 or tree2):
            return True
        elif tree1 and tree2:
            if tree1.val == tree2.val and \
                self.is_identical_tree(tree1.left, tree2.left) and \
                    self.is_identical_tree(tree1.right, tree2.right):
                return True
        else:
            return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.is_identical_tree(root, subRoot):
            return True
        elif root and (root.left or root.right):
            if root.left and root.right:
                return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
            elif root.right:
                return self.isSubtree(root.right, subRoot)
            else:
                return self.isSubtree(root.left, subRoot)
        else:
            return False


tree1 = TreeNode(1,
                 TreeNode(3,
                          TreeNode(5)),
                 TreeNode(2)
                 )

tree2 = TreeNode(2,
                 TreeNode(1,
                          None,
                          TreeNode(4)
                          ),
                 TreeNode(3,
                          None,
                          TreeNode(1,
                                   TreeNode(3,
                                            TreeNode(5)),
                                   TreeNode(2)
                                   )
                          )
                 )
print(Solution().isSubtree(tree2, tree1))


