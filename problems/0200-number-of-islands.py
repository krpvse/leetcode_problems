# 200. Number of Islands
# Difficulty: Medium
# Topics: Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix
# https://leetcode.com/problems/number-of-islands/
#
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return
# the number of islands.
#
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or
# vertically. You may assume all four edges of the grid are all surrounded by water.
#
# Example 1:
#
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
#
# Example 2:
#
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
#
# Constraints:
#
# - m == grid.length
# - n == grid[i].length
# - 1 <= m, n <= 300
# - grid[i][j] is '0' or '1'.

class Solution:
    
    def markIsland(self, grid: List[List[str]], m: int, n: int, i: int, j: int):
        grid[i][j] = "checked"
        if i+1 < m and grid[i+1][j] == "1":
            self.markIsland(grid, m, n, i+1, j)
        if i-1 >= 0 and grid[i-1][j] == "1":
            self.markIsland(grid, m, n, i-1, j)
        if j+1 < n and grid[i][j+1] == "1":
            self.markIsland(grid, m, n, i, j+1)
        if j-1 >= 0 and grid[i][j-1] == "1":
            self.markIsland(grid, m, n, i, j-1)

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        island_qty = 0
        for i in range(0, m, 1): 
            for j in range(0, n, 1):
                if grid[i][j] == "1":
                    island_qty += 1
                    self.markIsland(grid, m, n, i, j)

        return island_qty
