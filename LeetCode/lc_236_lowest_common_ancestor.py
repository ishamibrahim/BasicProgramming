from typing import List

from LeetCode.utils import TreeNode
"""
--medium--
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
Ex Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
                       3
                    /     \
                   5        1
                 /   \    /   \
                6    2   0     8
                   /   \
                  7     4
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

"""

class Solution:
    """
    Solution uses dynamic programming with DFS
    Runtime: 80%
    Memory: 13%
   """
    common_parent = None

    def get_matching_node(self, node, p, q):
        current_node = False
        if node:
            if node.val in (p.val, q.val):
                current_node = True
                if not node.left and not node.right:
                    return current_node
            l_found = self.get_matching_node(node.left, p, q)
            r_found = self.get_matching_node(node.right, p, q)
            if l_found or r_found:
                if l_found and r_found:
                    self.common_parent = node
                if current_node:
                    self.common_parent = node
            return l_found or r_found or current_node
        else:
            return current_node

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        _ = self.get_matching_node(root, p, q)
        return self.common_parent


bin_tree = TreeNode(3,
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
p = TreeNode(6)
q = TreeNode(4)
print(Solution().lowestCommonAncestor(bin_tree, p, q))
