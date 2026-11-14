# 977. Squares of a Sorted Array
# Difficulty: Easy
# Topics: Array, Two Pointers, Sorting
# https://leetcode.com/problems/squares-of-a-sorted-array/
#
# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each
# number sorted in non-decreasing order.
#
# Example 1:
#
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
#
# Example 2:
#
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
#
# Constraints:
#
# - 1 <= nums.length <= 10^4
# - -10^4 <= nums[i] <= 10^4
# - nums is sorted in non-decreasing order.
#
# Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n)
# solution using a different approach?

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        qty = len(nums)
        
        # Ищем отрицательный и положительный
        i = None
        j = None
        for k in range(0, qty, 1):
            if nums[k] < 0:
                i = k
            else:
                j = k
                break
        
        # Образование нового массива
        res = []
        while (i is not None and i >= 0) or (j is not None and j < qty):
            if (i is not None and i >= 0) and (j is not None and j < qty):
                d1 = nums[i] * nums[i]
                d2 = nums[j] * nums[j]
                if d1 < d2:
                    d = d1
                    i -= 1
                else:
                    d = d2
                    j += 1
            elif i is not None and i >= 0:
                d = nums[i] * nums[i]
                i -= 1
            elif j is not None and j < qty:
                d = nums[j] * nums[j]
                j += 1
            res.append(d)

        return res
