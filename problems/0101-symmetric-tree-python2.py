# 101. Symmetric Tree
# Difficulty: Easy
# Topics: Tree, Depth-First Search, Breadth-First Search, Binary Tree
# https://leetcode.com/problems/symmetric-tree/
#
# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its
# center).
#
# Example 1:
#
# [image: https://assets.leetcode.com/uploads/2021/02/19/symtree1.jpg]
#
# Input: root = [1,2,2,3,4,4,3]
# Output: true
#
# Example 2:
#
# [image: https://assets.leetcode.com/uploads/2021/02/19/symtree2.jpg]
#
# Input: root = [1,2,2,null,3,null,3]
# Output: false
#
# Constraints:
#
# - The number of nodes in the tree is in the range [1, 1000].
# - -100 <= Node.val <= 100
#
# Follow up: Could you solve it both recursively and iteratively?

class Solution(object):
    
    def isMirror(self, a, b):
        if not a and not b:
            return True
        elif a and not b:
            return False
        elif b and not a:
            return False
        elif a.val != b.val:
            return False

        res1 = self.isMirror(a.left, b.right)
        res2 = self.isMirror(a.right, b.left)

        return bool(res1 and res2)

    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self.isMirror(root.left, root.right)
