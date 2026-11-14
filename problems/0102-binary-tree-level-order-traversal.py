# 102. Binary Tree Level Order Traversal
# Difficulty: Medium
# Topics: Tree, Breadth-First Search, Binary Tree
# https://leetcode.com/problems/binary-tree-level-order-traversal/
#
# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from
# left to right, level by level).
#
# Example 1:
#
# [image: https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg]
#
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
#
# Example 2:
#
# Input: root = [1]
# Output: [[1]]
#
# Example 3:
#
# Input: root = []
# Output: []
#
# Constraints:
#
# - The number of nodes in the tree is in the range [0, 2000].
# - -1000 <= Node.val <= 1000

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []    
        
        result = [[root.val]]
        
        current_level = []
        if root.left is not None:
            current_level.append(root.left)
        if root.right is not None:
            current_level.append(root.right)

        while len(current_level) > 0:
            new_level = []
            level_result = []
            for node in current_level:
                level_result.append(node.val)
                left = node.left
                right = node.right
                if left is not None:
                    new_level.append(left)
                if right is not None:
                    new_level.append(right)
            result.append(level_result)
            current_level = new_level

        return result
