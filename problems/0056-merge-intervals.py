# 56. Merge Intervals
# Difficulty: Medium
# Topics: Array, Sorting, Quicksort
# https://leetcode.com/problems/merge-intervals/
#
# Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals,
# and return an array of the non-overlapping intervals that cover all the intervals in the input.
#
# Example 1:
#
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
#
# Example 2:
#
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
#
# Example 3:
#
# Input: intervals = [[4,7],[1,4]]
# Output: [[1,7]]
# Explanation: Intervals [1,4] and [4,7] are considered overlapping.
#
# Constraints:
#
# - 1 <= intervals.length <= 10^4
# - intervals[i].length == 2
# - 0 <= start_i <= end_i <= 10^4

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        qty = len(intervals)
        if qty == 1:
            return intervals

        # Сортировка, сложность Onlogn
        intervals.sort(key=lambda x: x[0])
        
        # Объединение интервалов, сложность On
        res = []
        
        left = intervals[0][0]
        right = intervals[0][1]
        for i in range(1, qty, 1):
            interval = intervals[i]
            l = interval[0]
            r = interval[1]

            if right >= l or left == l:
                right = r if r > right else right
            else:
                res.append([left, right])
                left = l
                right = r
            
        res.append([left, right])
        return res
