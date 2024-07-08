import heapq
from typing import Optional

from LeetCode.utils import TreeNode
from collections import deque

"""
    --hard--
    https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
    Given the root of a binary tree, return the maximum path sum of any non-empty path.A path in a binary tree is a 
    sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only 
    appear in the sequence at most once. Note that the path does not need to pass through the root.
    
    
"""


class Solution:

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        This is a neetcode solution.

        """
        result = [root.val] # using list instead of an integer because list is going to be referenced.

        def dfs(node):
            if not node:
                return 0
            max_left = dfs(node.left)
            max_right = dfs(node.right)
            max_left = max(max_left, 0)
            max_right = max(max_right, 0)

            result[0] = max(result[0], node.val + max_left + max_right)
            return max(node.val + max_left, node.val + max_right)

        dfs(root)
        return result[0]


bin_tree = TreeNode(-1,
                    TreeNode(5,
                             TreeNode(4,
                                      None,
                                      TreeNode(2,
                                               TreeNode(-4),
                                               None)
                                      ),
                             None
                             ),
                    None
                    )

bin_tree = TreeNode(-1,
                    TreeNode(8,
                             None,
                             TreeNode(-9)),
                    TreeNode(2,
                             TreeNode(0,
                                      TreeNode(-3,
                                               None,
                                               TreeNode(-9,
                                                        None,
                                                        TreeNode(2)
                                                        )
                                               )
                                      )
                             )
                    )

print(Solution().maxPathSum(bin_tree))
