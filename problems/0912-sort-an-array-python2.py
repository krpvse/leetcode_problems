# 912. Sort an Array
# Difficulty: Medium
# Topics: Array, Divide and Conquer, Sorting, Heap (Priority Queue), Merge Sort, Bucket Sort, Radix Sort, Counting Sort
# https://leetcode.com/problems/sort-an-array/
#
# Given an array of integers nums, sort the array in ascending order and return it.
#
# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and
# with the smallest space complexity possible.
#
# Example 1:
#
# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
#
# Example 2:
#
# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
# Explanation: Note that the values of nums are not necessarily unique.
#
# Constraints:
#
# - 1 <= nums.length <= 5 * 10^4
# - -5 * 10^4 <= nums[i] <= 5 * 10^4

import random


class Solution(object):
    
    def quickSort(self, arr, first, last):
        if first >= last:
            return
        elif len(arr) <= 1:
            return arr

        n = arr[random.randint(first, last)]
        i, j = first, last

        while i <= j:
            while arr[i] < n:
                i += 1
            while arr[j] > n:
                j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
        
        self.quickSort(arr, first, j)
        self.quickSort(arr, i, last)
    

    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.quickSort(nums, 0, len(nums)-1)
        return nums
