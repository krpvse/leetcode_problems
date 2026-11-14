# 1572. Matrix Diagonal Sum
# Difficulty: Easy
# Topics: Array, Matrix
# https://leetcode.com/problems/matrix-diagonal-sum/
#
# Given a square matrix mat, return the sum of the matrix diagonals.
#
# Only include the sum of all the elements on the primary diagonal and all the elements on the
# secondary diagonal that are not part of the primary diagonal.
#
# Example 1:
#
# [image: https://assets.leetcode.com/uploads/2020/08/14/sample_1911.png]
#
# Input: mat = [[1,2,3],
#               [4,5,6],
#               [7,8,9]]
# Output: 25
# Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
# Notice that element mat[1][1] = 5 is counted only once.
#
# Example 2:
#
# Input: mat = [[1,1,1,1],
#               [1,1,1,1],
#               [1,1,1,1],
#               [1,1,1,1]]
# Output: 8
#
# Example 3:
#
# Input: mat = [[5]]
# Output: 5
#
# Constraints:
#
# - n == mat.length == mat[i].length
# - 1 <= n <= 100
# - 1 <= mat[i][j] <= 100

class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        
        n = len(mat)

        row1, col1 = 0, 0
        row2, col2 = 0, n-1
        row3, col3 = n-1, 0
        row4, col4 = n-1, n-1

        res = 0
        while row1 <= row4:
            if row1 == row4 and col1 == col4:
                res += mat[row1][col1]
                break
            
            val1 = mat[row1][col1]
            val2 = mat[row2][col2]
            val3 = mat[row3][col3]
            val4 = mat[row4][col4]
            res = res + val1 + val2 + val3 + val4

            row1 += 1
            col1 += 1
            row2 += 1
            col2 -= 1
            row3 -= 1
            col3 += 1
            row4 -= 1
            col4 -= 1
    
        return res
