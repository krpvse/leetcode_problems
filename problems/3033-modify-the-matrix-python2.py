# 3033. Modify the Matrix
# Difficulty: Easy
# Topics: Array, Matrix
# https://leetcode.com/problems/modify-the-matrix/
#
# Given a 0-indexed m x n integer matrix matrix, create a new 0-indexed matrix called answer. Make
# answer equal to matrix, then replace each element with the value -1 with the maximum element in its
# respective column.
#
# Return the matrix answer.
#
# Example 1:
#
# [image: https://assets.leetcode.com/uploads/2023/12/24/matrix1.png]
#
# Input: matrix = [[1,2,-1],[4,-1,6],[7,8,9]]
# Output: [[1,2,9],[4,8,6],[7,8,9]]
# Explanation: The diagram above shows the elements that are changed (in blue).
# - We replace the value in the cell [1][1] with the maximum value in the column 1, that is 8.
# - We replace the value in the cell [0][2] with the maximum value in the column 2, that is 9.
#
# Example 2:
#
# [image: https://assets.leetcode.com/uploads/2023/12/24/matrix2.png]
#
# Input: matrix = [[3,-1],[5,2]]
# Output: [[3,2],[5,2]]
# Explanation: The diagram above shows the elements that are changed (in blue).
#
# Constraints:
#
# - m == matrix.length
# - n == matrix[i].length
# - 2 <= m, n <= 50
# - -1 <= matrix[i][j] <= 100
# - The input is generated such that each column contains at least one non-negative integer.

class Solution(object):
    def modifiedMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        
        m = len(matrix)
        n = len(matrix[0])

        for j in range(0, n, 1):
            max_val = -1
            inds = []
            for i in range(0, m, 1):
                val = matrix[i][j]
                if val > max_val:
                    max_val = val
                elif val == -1:
                    inds.append((i, j))
            for ind in inds:
                matrix[ind[0]][ind[1]] = max_val
 
        return matrix
