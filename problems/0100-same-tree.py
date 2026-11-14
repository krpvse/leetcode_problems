# 100. Same Tree
# Difficulty: Easy
# Topics: Tree, Depth-First Search, Breadth-First Search, Binary Tree
# https://leetcode.com/problems/same-tree/
#
# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
#
# Two binary trees are considered the same if they are structurally identical, and the nodes have the
# same value.
#
# Example 1:
#
# [image: https://assets.leetcode.com/uploads/2020/12/20/ex1.jpg]
#
# Input: p = [1,2,3], q = [1,2,3]
# Output: true
#
# Example 2:
#
# [image: https://assets.leetcode.com/uploads/2020/12/20/ex2.jpg]
#
# Input: p = [1,2], q = [1,null,2]
# Output: false
#
# Example 3:
#
# [image: https://assets.leetcode.com/uploads/2020/12/20/ex3.jpg]
#
# Input: p = [1,2,1], q = [1,1,2]
# Output: false
#
# Constraints:
#
# - The number of nodes in both trees is in the range [0, 100].
# - -10^4 <= Node.val <= 10^4

class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if not p and not q:
            return True
        elif not p and q:
            return False
        elif p and not q:
            return False
        elif p.val != q.val:
            return False
        
        res1 = self.isSameTree(p.left, q.left)
        res2 = self.isSameTree(p.right, q.right)

        return bool(res1 and res2)
