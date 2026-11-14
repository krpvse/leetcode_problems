# 283. Move Zeroes
# Difficulty: Easy
# Topics: Array, Two Pointers
# https://leetcode.com/problems/move-zeroes/
#
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of
# the non-zero elements.
#
# Note that you must do this in-place without making a copy of the array.
#
# Example 1:
#
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
#
# Example 2:
#
# Input: nums = [0]
# Output: [0]
#
# Constraints:
#
# - 1 <= nums.length <= 10^4
# - -2^31 <= nums[i] <= 2^31 - 1
#
# Follow up: Could you minimize the total number of operations done?

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        qty = len(nums)
        
        # Ищем ненулевой последний элемент
        j = qty - 1
        while nums[j] == 0:
            j -= 1
            if j <= 0:
                return nums

        # Переносим нули в конец
        i = 0
        while i < j:
            if nums[i] == 0:
                k = i
                g = i + 1
                while g <= j:
                    nums[k], nums[g] = nums[g], nums[k]
                    k += 1
                    g += 1
                j -= 1
            if nums[i] != 0:
                i += 1

        return nums
