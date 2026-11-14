# 763. Partition Labels
# Difficulty: Medium
# Topics: Hash Table, Two Pointers, String, Greedy
# https://leetcode.com/problems/partition-labels/
#
# You are given a string s. We want to partition the string into as many parts as possible so that
# each letter appears in at most one part. For example, the string "ababcc" can be partitioned into
# ["abab", "cc"], but partitions such as ["aba", "bcc"] or ["ab", "ab", "cc"] are invalid.
#
# Note that the partition is done so that after concatenating all the parts in order, the resultant
# string should be s.
#
# Return a list of integers representing the size of these parts.
#
# Example 1:
#
# Input: s = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
#
# Example 2:
#
# Input: s = "eccbbbbdec"
# Output: [10]
#
# Constraints:
#
# - 1 <= s.length <= 500
# - s consists of lowercase English letters.

class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        qty = len(s)
        if qty == 1:
            return [1]

        res = []
        checked = set()

        left = right = i = 0
        while right <= qty - 1:
            while i <= right:
                if s[i] not in checked:
                    for j in range(i, qty, 1):
                        if s[j] == s[i] and right < j:
                            right = j
                    checked.add(s[i])
                i += 1
            res.append(right-left+1)

            right += 1
            left = right

        return res
