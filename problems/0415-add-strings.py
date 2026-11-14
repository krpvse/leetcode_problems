# 415. Add Strings
# Difficulty: Easy
# Topics: Math, String, Simulation
# https://leetcode.com/problems/add-strings/
#
# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and
# num2 as a string.
#
# You must solve the problem without using any built-in library for handling large integers (such as
# BigInteger). You must also not convert the inputs to integers directly.
#
# Example 1:
#
# Input: num1 = "11", num2 = "123"
# Output: "134"
#
# Example 2:
#
# Input: num1 = "456", num2 = "77"
# Output: "533"
#
# Example 3:
#
# Input: num1 = "0", num2 = "0"
# Output: "0"
#
# Constraints:
#
# - 1 <= num1.length, num2.length <= 10^4
# - num1 and num2 consist of only digits.
# - num1 and num2 don't have any leading zeros except for the zero itself.

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        res = ""

        i = len(num1) - 1
        j = len(num2) - 1
        remembered = 0
        while i >= 0 or j >= 0:
            if i >= 0 and j >= 0:
                d = int(num1[i]) + int(num2[j]) + remembered
                i -= 1
                j -= 1
            elif i >= 0:
                d = int(num1[i]) + remembered
                i -= 1
            else:
                d = int(num2[j]) + remembered
                j -= 1
            
            res = str(d)[-1] + res
            remembered = 1 if d >= 10 else 0

        if remembered == 1:
            res = str(1) + res

        return res
