# 219. Contains Duplicate II
# Difficulty: Easy
# Topics: Array, Hash Table, Sliding Window
# https://leetcode.com/problems/contains-duplicate-ii/
#
# Given an integer array nums and an integer k, return true if there are two distinct indices i and j
# in the array such that nums[i] == nums[j] and abs(i - j) <= k.
#
# Example 1:
#
# Input: nums = [1,2,3,1], k = 3
# Output: true
#
# Example 2:
#
# Input: nums = [1,0,1,1], k = 1
# Output: true
#
# Example 3:
#
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
#
# Constraints:
#
# - 1 <= nums.length <= 10^5
# - -10^9 <= nums[i] <= 10^9
# - 0 <= k <= 10^5

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        qty = len(nums)
        if qty == 1:
            return False
        
        i = 0
        j = k
        
        # Создаем первый отрезок
        uniq = set()
        for n in range(i, j+1, 1):
            if n >= qty:
                return False
                
            num = nums[n]
            if num in uniq:
                return True
            uniq.add(num)

        # Двигаем отрезок
        old_num = nums[i]
        
        i += 1
        j += 1
        while j < qty:
            uniq.remove(old_num)
            
            new_num = nums[j]
            if new_num in uniq:
                return True
            uniq.add(new_num)
            
            old_num = nums[i]

            i += 1
            j += 1
        
        return False
