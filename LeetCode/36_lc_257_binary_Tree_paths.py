from typing import Optional, List

from LeetCode.utils import TreeNode
"""
--easy--
Given the root of a binary tree, return all root-to-leaf paths in any order.

The below solution takes a DFS approach using recursion
Solution -  Runtime: 96%
            Memory: 20%

"""

class Solution:
    def find_str_till_node(self, node: Optional[TreeNode], path: str, nodes_list: List[str]) :
        path += f"->{node.val}"
        if not (node.left or node.right):
            nodes_list.append(path)
        else:
            if node.left:
                self.find_str_till_node(node.left, path, nodes_list)
            if node.right:
                self.find_str_till_node(node.right, path, nodes_list)

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result_list = []
        if root:
            path = f"{root.val}"
            if root.left:
                self.find_str_till_node(root.left, path, result_list)
            if root.right:
                self.find_str_till_node(root.right, path, result_list)
            if not (root.left or root.right):
                result_list.append(path)
        return result_list


tree = TreeNode("A", TreeNode("B", TreeNode("E"), TreeNode("F", TreeNode("G"))), TreeNode("C"))

print(Solution().binaryTreePaths(tree))
