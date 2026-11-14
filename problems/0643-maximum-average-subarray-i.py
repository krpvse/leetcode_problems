# 643. Maximum Average Subarray I
# Difficulty: Easy
# Topics: Array, Sliding Window
# https://leetcode.com/problems/maximum-average-subarray-i/
#
# You are given an integer array nums consisting of n elements, and an integer k.
#
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return
# this value. Any answer with a calculation error less than 10^-5 will be accepted.
#
# Example 1:
#
# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
#
# Example 2:
#
# Input: nums = [5], k = 1
# Output: 5.00000
#
# Constraints:
#
# - n == nums.length
# - 1 <= k <= n <= 10^5
# - -10^4 <= nums[i] <= 10^4

class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        qty = len(nums)
        
        l = 0
        r = k - 1

        # Находим сумму и среднее первого отрезка
        summ = 0
        for i in range(l, k, 1):
            summ += nums[i]
        avg = summ / k

        # Двигаем окно и ищем максимальное среднее
        old_left = nums[l]
        old_right = nums[r]

        while r + 1 < qty:
            r += 1
            l += 1

            new_left = nums[l]
            new_right = nums[r]
            
            summ = summ - old_left + new_right
            new_avg = summ / k
            avg = new_avg if new_avg > avg else avg
            
            old_left = new_left
            old_right = new_right
    
        return avg
