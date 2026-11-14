# 257. Binary Tree Paths
# Difficulty: Easy
# Topics: String, Backtracking, Tree, Depth-First Search, Binary Tree
# https://leetcode.com/problems/binary-tree-paths/
#
# You are given the root of a binary tree.
#
# Return all root-to-leaf paths in any order.
#
# A leaf is a node with no children.
#
# Example 1:
#
# [image: https://assets.leetcode.com/uploads/2021/03/12/paths-tree.jpg]
#
# Input: root = [1,2,3,null,5]
# Output: ["1->2->5","1->3"]
#
# Example 2:
#
# Input: root = [1]
# Output: ["1"]
#
# Constraints:
#
# - The number of nodes in the tree is in the range [1, 100].
# - -100 <= Node.val <= 100

class Solution(object):

    def path(self, node, allPaths, curPath = ""):
        if curPath == "":
            curPath = str(node.val)
        else:
            curPath = curPath + "->" + str(node.val)
        
        if not node.left and not node.right:
            allPaths.append(curPath)
            return
        if node.left:
            self.path(node.left, allPaths, curPath)
        if node.right:
            self.path(node.right, allPaths, curPath)

    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        allPaths = []
        self.path(root, allPaths)
        return allPaths
