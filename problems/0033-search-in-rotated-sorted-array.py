# 33. Search in Rotated Sorted Array
# Difficulty: Medium
# Topics: Array, Binary Search
# https://leetcode.com/problems/search-in-rotated-sorted-array/
#
# There is an integer array nums sorted in ascending order (with distinct values).
#
# Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k
# < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0],
# nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3
# indices and become [4,5,6,7,0,1,2].
#
# Given the array nums after the possible rotation and an integer target, return the index of target
# if it is in nums, or -1 if it is not in nums.
#
# You must write an algorithm with O(log n) runtime complexity.
#
# Example 1:
#
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
#
# Example 2:
#
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
#
# Example 3:
#
# Input: nums = [1], target = 0
# Output: -1
#
# Constraints:
#
# - 1 <= nums.length <= 5000
# - -10^4 <= nums[i] <= 10^4
# - All values of nums are unique.
# - nums is an ascending array that is possibly rotated.
# - -10^4 <= target <= 10^4

class Solution:
    
    def bs_classic(self, nums: list[int], target: int) -> int:
        left = -1
        right = len(nums) - 1

        while left + 1 != right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid
            else:
                right = mid
        
        return right


    def bs_reversed(self, nums: list[int], target: int) -> int:
        # Определяем, в какой части находится target
        first = nums[0]
        if target > first:
            place = "left"
        else:
            place = "right" 
        
        # Бинарный поиск
        left = 0
        right = len(nums) - 1

        while left + 1 != right:
            mid = (left + right) // 2
            if place == "left" and first > nums[mid]:
                right = mid
            elif place == "right" and first <= nums[mid]:
                left = mid
            
            elif place == "left" and first <= nums[mid]:
                if target > nums[mid]:
                    left = mid
                else:
                    right = mid
            elif place == "right" and first > nums[mid]:
                if target > nums[mid]:
                    left = mid
                else:
                    right = mid
        
        return right
            

    def search(self, nums: list[int], target: int) -> int:
        qty = len(nums)
        if qty == 1:
            res = 0 if nums[0] == target else -1
            return res
        
        # Проверка крайних элементов
        first = nums[0]
        if first == target:
            return 0
        last = nums[qty-1]
        if last == target:
            return qty - 1

        # Бинарный поиск
        if nums[0] > nums[qty-1]:
            res = self.bs_reversed(nums, target)
        else:
            res = self.bs_classic(nums, target)
        
        res = res if nums[res] == target else -1
        return res
