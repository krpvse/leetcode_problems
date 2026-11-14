# 3242. Design Neighbor Sum Service
# Difficulty: Easy
# Topics: Array, Hash Table, Design, Matrix, Simulation
# https://leetcode.com/problems/design-neighbor-sum-service/
#
# You are given a n x n 2D array grid containing distinct elements in the range [0, n^2 - 1].
#
# Implement the NeighborSum class:
#
# - NeighborSum(int [][]grid) initializes the object.
# - int adjacentSum(int value) returns the sum of elements which are adjacent neighbors of value, that
#   is either to the top, left, right, or bottom of value in grid.
# - int diagonalSum(int value) returns the sum of elements which are diagonal neighbors of value, that
#   is either to the top-left, top-right, bottom-left, or bottom-right of value in grid.
#
# [image: https://assets.leetcode.com/uploads/2024/06/24/design.png]
#
# Example 1:
#
# Input:
#
# ["NeighborSum", "adjacentSum", "adjacentSum", "diagonalSum", "diagonalSum"]
#
# [[[[0, 1, 2], [3, 4, 5], [6, 7, 8]]], [1], [4], [4], [8]]
#
# Output: [null, 6, 16, 16, 4]
#
# Explanation:
#
# [image: https://assets.leetcode.com/uploads/2024/06/24/designexample0.png]
#
# - The adjacent neighbors of 1 are 0, 2, and 4.
# - The adjacent neighbors of 4 are 1, 3, 5, and 7.
# - The diagonal neighbors of 4 are 0, 2, 6, and 8.
# - The diagonal neighbor of 8 is 4.
#
# Example 2:
#
# Input:
#
# ["NeighborSum", "adjacentSum", "diagonalSum"]
#
# [[[[1, 2, 0, 3], [4, 7, 15, 6], [8, 9, 10, 11], [12, 13, 14, 5]]], [15], [9]]
#
# Output: [null, 23, 45]
#
# Explanation:
#
# [image: https://assets.leetcode.com/uploads/2024/06/24/designexample2.png]
#
# - The adjacent neighbors of 15 are 0, 10, 7, and 6.
# - The diagonal neighbors of 9 are 4, 12, 14, and 15.
#
# Constraints:
#
# - 3 <= n == grid.length == grid[0].length <= 10
# - 0 <= grid[i][j] <= n^2 - 1
# - All grid[i][j] are distinct.
# - value in adjacentSum and diagonalSum will be in the range [0, n^2 - 1].
# - At most 2 * n^2 calls will be made to adjacentSum and diagonalSum.

class NeighborSum(object):

    def __init__(self, grid):
        """
        :type grid: List[List[int]]
        """
        self.grid = grid
        self.n = len(grid)


    def adjacentSum(self, value):
        """
        :type value: int
        :rtype: int
        """
        s = 0
        for i in range(0, self.n, 1):
            for j in range(0, self.n, 1):
                if self.grid[i][j] == value:
                    if i - 1 >= 0:
                        s += self.grid[i-1][j]
                    if i + 1 <= self.n - 1:
                        s += self.grid[i+1][j]
                    if j - 1 >= 0:
                        s += self.grid[i][j-1]
                    if j + 1 <= self.n - 1:
                        s += self.grid[i][j+1]
                    return s
        return s

    def diagonalSum(self, value):
        """
        :type value: int
        :rtype: int
        """
        s = 0
        for i in range(0, self.n, 1):
            for j in range(0, self.n, 1):
                if self.grid[i][j] == value:
                    if i - 1 >= 0:
                        if j - 1 >= 0:
                            s += self.grid[i-1][j-1]
                        if j + 1 <= self.n - 1:
                            s += self.grid[i-1][j+1]
                    if i + 1 <= self.n - 1:
                        if j - 1 >= 0:
                            s += self.grid[i+1][j-1]
                        if j + 1 <= self.n - 1:
                            s += self.grid[i+1][j+1]
                    return s
        return s


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)
