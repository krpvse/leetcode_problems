# 20. Valid Parentheses
# Difficulty: Easy
# Topics: String, Stack, Bracket Sequences
# https://leetcode.com/problems/valid-parentheses/
#
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the
# input string is valid.
#
# An input string is valid if:
#
# - Open brackets must be closed by the same type of brackets.
# - Open brackets must be closed in the correct order.
# - Every close bracket has a corresponding open bracket of the same type.
#
# Example 1:
#
# Input: s = "()"
#
# Output: true
#
# Example 2:
#
# Input: s = "()[]{}"
#
# Output: true
#
# Example 3:
#
# Input: s = "(]"
#
# Output: false
#
# Example 4:
#
# Input: s = "([])"
#
# Output: true
#
# Example 5:
#
# Input: s = "([)]"
#
# Output: false
#
# Constraints:
#
# - 1 <= s.length <= 10^4
# - s consists of parentheses only '()[]{}'.

class Solution:
    def isValid(self, s: str) -> bool:
        res = True
        opens = []
        
        for ch in s:
            if ch in (")", "}", "]"):
                if not opens:
                    res = False
                    break
                last_ch = opens.pop()
                if ch == ")":
                    if last_ch != "(":
                        res = False
                        break
                elif ch == "}":
                    if last_ch != "{":
                        res = False
                        break
                elif ch == "]":
                    if last_ch != "[":
                        res = False
                        break
            else:
                opens.append(ch)
        
        if opens:
            res = False
        
        return res
