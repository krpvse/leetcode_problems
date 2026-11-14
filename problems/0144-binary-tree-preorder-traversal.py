# 144. Binary Tree Preorder Traversal
# Difficulty: Easy
# Topics: Stack, Tree, Depth-First Search, Binary Tree
# https://leetcode.com/problems/binary-tree-preorder-traversal/
#
# Given the root of a binary tree, return the preorder traversal of its nodes' values.
#
# Example 1:
#
# Input: root = [1,null,2,3]
#
# Output: [1,2,3]
#
# Explanation:
#
# [image: https://assets.leetcode.com/uploads/2024/08/29/screenshot-2024-08-29-202743.png]
#
# Example 2:
#
# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
#
# Output: [1,2,4,5,6,7,3,8,9]
#
# Explanation:
#
# [image: https://assets.leetcode.com/uploads/2024/08/29/tree_2.png]
#
# Example 3:
#
# Input: root = []
#
# Output: []
#
# Example 4:
#
# Input: root = [1]
#
# Output: [1]
#
# Constraints:
#
# - The number of nodes in the tree is in the range [0, 100].
# - -100 <= Node.val <= 100
#
# Follow up: Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _preorderTraversal(
        self, 
        node: Optional[TreeNode],
        result: list = None
    ) -> List[int]:
        if result is None:
            result = []
        if node is None:
            return
        result.append(node.val)
        self._preorderTraversal(node.left, result)
        self._preorderTraversal(node.right, result)
        return result

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        return self._preorderTraversal(root)
