# 111. Minimum Depth of Binary Tree
# Difficulty: Easy
# Topics: Tree, Depth-First Search, Breadth-First Search, Binary Tree
# https://leetcode.com/problems/minimum-depth-of-binary-tree/
#
# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path from the root node down to the
# nearest leaf node.
#
# Note: A leaf is a node with no children.
#
# Example 1:
#
# [image: https://assets.leetcode.com/uploads/2020/10/12/ex_depth.jpg]
#
# Input: root = [3,9,20,null,null,15,7]
# Output: 2
#
# Example 2:
#
# Input: root = [2,null,3,null,4,null,5,null,6]
# Output: 5
#
# Constraints:
#
# - The number of nodes in the tree is in the range [0, 10^5].
# - -1000 <= Node.val <= 1000

class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        
        left = root.left
        right = root.right
        
        if not left and not right:
            return 1
        elif left and not right:
            res = self.minDepth(left)
        elif not left and right:
            res = self.minDepth(right)
        else:
            res1 = self.minDepth(root.left)
            res2 = self.minDepth(root.right)
            res = min(res1, res2)

        return 1 + res
