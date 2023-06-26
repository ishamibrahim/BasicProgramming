from typing import Optional, List

from LeetCode.constants import TreeNode
"""
https://leetcode.com/problems/average-of-levels-in-binary-tree

Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. 
Answers within 10-5 of the actual answer will be accepted. 

Solution -  Runtime: 84%
            Memory:  8.1%
"""

class Solution:
    def __init__(self, ):
        self.levels = dict()

    def add_to_list(self, level: int, node: TreeNode):
        if node:
            if self.levels.get(level, None) is not None:
                self.levels[level].append(node.val)
            else:
                self.levels[level] = [node.val]
            self.add_to_list(level+1, node.left)
            self.add_to_list(level+1, node.right)

    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # Using a depth first search
        self.add_to_list(0, root)
        return [sum(val_list)/len(val_list) for val_list in self.levels.values()]


tree = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(3)), TreeNode(2, TreeNode(3)))

print(Solution().averageOfLevels(tree))

