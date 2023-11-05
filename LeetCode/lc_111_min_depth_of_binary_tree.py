from typing import Optional
from LeetCode.utils import TreeNode
"""
    https://leetcode.com/problems/minimum-depth-of-binary-tree
    Given a binary tree, find its minimum depth.
    The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
    
    
    Solution -  Runtime : 74%
                Memory: 42.5%
"""

class Solution:
    def __init__(self):
        self.min_depth = pow(10, 30)

    def find_min_depth(self, node: TreeNode, level: int ):
        if not (node.left or node.right):
                self.min_depth = min(self.min_depth, level)
        else:
            if node.left:
                self.find_min_depth(node.left, level+1)
            if node.right:
                self.find_min_depth(node.right, level+1)

    def minDepth(self, root: Optional[TreeNode]) -> int:
        # This solution is a DFS solution where it checks every node if its a leaf and returns the level if
        # its level is lesser than the self.min_depth value
        if root:
            level = 1
            self.find_min_depth(root, level)
            return self.min_depth

        return 0

tree1  = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(8)), TreeNode(5)), TreeNode(3, None, TreeNode(7)))
tree2 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(Solution().minDepth(tree2))

