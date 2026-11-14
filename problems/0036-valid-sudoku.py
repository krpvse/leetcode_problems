# 36. Valid Sudoku
# Difficulty: Medium
# Topics: Array, Hash Table, Matrix
# https://leetcode.com/problems/valid-sudoku/
#
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to
# the following rules:
#
# - Each row must contain the digits 1-9 without repetition.
# - Each column must contain the digits 1-9 without repetition.
# - Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
#
# Note:
#
# - A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# - Only the filled cells need to be validated according to the mentioned rules.
#
# Example 1:
#
# [image: https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-
# Sudoku-by-L2G-20050714.svg.png]
#
# Input: board =
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true
#
# Example 2:
#
# Input: board =
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
#
# Constraints:
#
# - board.length == 9
# - board[i].length == 9
# - board[i][j] is a digit 1-9 or '.'.

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        temp_box1 = []
        temp_box2 = []
        temp_box3 = []
        
        for i in range(0, len(board), 1):
            temp_row = []
            temp_column = []
            for j in range(0, len(board[i]), 1):
                if board[i][j] != ".":
                    if board[i][j] not in temp_row:
                        temp_row.append(board[i][j])
                    else:
                        print("Не проходит по 1 правилу")
                        return False
                if board[j][i] != ".":
                    if board[j][i] not in temp_column:
                        temp_column.append(board[j][i])
                    else:
                        print("Не проходит по 2 правилу")
                        return False

                if j <= 2:
                    if board[i][j] != ".":
                        if board[i][j] not in temp_box1:
                            temp_box1.append(board[i][j])
                        else:
                            print("Не проходит по 3 правилу - 1")
                            return False
                elif j <= 5:
                    if board[i][j] != ".":
                        if board[i][j] not in temp_box2:
                            temp_box2.append(board[i][j])
                        else:
                            print("Не проходит по 3 правилу - 2")
                            return False
                else:
                    if board[i][j] != ".":
                        if board[i][j] not in temp_box3:
                            temp_box3.append(board[i][j])
                        else:
                            print("Не проходит по 3 правилу - 3")
                            return False

            if (i + 1) % 3 == 0:
                temp_box1 = []
                temp_box2 = []
                temp_box3 = []
        
        return True
