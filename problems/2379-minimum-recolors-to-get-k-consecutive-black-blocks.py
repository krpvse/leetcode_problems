# 2379. Minimum Recolors to Get K Consecutive Black Blocks
# Difficulty: Easy
# Topics: String, Sliding Window
# https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/
#
# You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B',
# representing the color of the i^th block. The characters 'W' and 'B' denote the colors white and
# black, respectively.
#
# You are also given an integer k, which is the desired number of consecutive black blocks.
#
# In one operation, you can recolor a white block such that it becomes a black block.
#
# Return the minimum number of operations needed such that there is at least one occurrence of k
# consecutive black blocks.
#
# Example 1:
#
# Input: blocks = "WBBWWBBWBW", k = 7
# Output: 3
# Explanation:
# One way to achieve 7 consecutive black blocks is to recolor the 0th, 3rd, and 4th blocks
# so that blocks = "BBBBBBBWBW".
# It can be shown that there is no way to achieve 7 consecutive black blocks in less than 3 operations.
# Therefore, we return 3.
#
# Example 2:
#
# Input: blocks = "WBWBBBW", k = 2
# Output: 0
# Explanation:
# No changes need to be made, since 2 consecutive black blocks already exist.
# Therefore, we return 0.
#
# Constraints:
#
# - n == blocks.length
# - 1 <= n <= 100
# - blocks[i] is either 'W' or 'B'.
# - 1 <= k <= n

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        qty = len(blocks)
        if qty < k:
            return 0
        
        left = 0
        right = k - 1

        # Определяем кол-во белых на первом отрезке
        current_white_qty = 0
        for i in range(left, right+1, 1):
            if blocks[i] == "W":
                current_white_qty += 1
        old_left = blocks[left]
        old_right = blocks[right]

        # Двигаем окно и сравниваем кол-во белых
        min_white_qty = current_white_qty

        left += 1
        right += 1
        while min_white_qty > 0 and right < qty:
            new_left = blocks[left]
            new_right = blocks[right]

            if old_left == "W":
                current_white_qty -= 1
            if new_right == "W":
                current_white_qty += 1
            
            if min_white_qty > current_white_qty:
                min_white_qty = current_white_qty
            
            old_left = new_left
            old_right = new_right
            
            left += 1
            right += 1


        return min_white_qty
