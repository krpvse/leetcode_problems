# 125. Valid Palindrome
# Difficulty: Easy
# Topics: Two Pointers, String
# https://leetcode.com/problems/valid-palindrome/
#
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and
# removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric
# characters include letters and numbers.
#
# Given a string s, return true if it is a palindrome, or false otherwise.
#
# Example 1:
#
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
#
# Example 2:
#
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
#
# Example 3:
#
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
#
# Constraints:
#
# - 1 <= s.length <= 2 * 10^5
# - s consists only of printable ASCII characters.

from string import ascii_lowercase, digits


ALLOWED_CHARS = ascii_lowercase + digits


class Solution:

    def find_next_allowed_char(
        self, 
        s: str, 
        start: int, 
        step: int,
        allowed_chars: list = ALLOWED_CHARS,
    ) -> tuple:
        qty = len(s)
        i = start
        while 0 <= i < qty:
            ch = s[i].lower()
            if ch.isalnum():
                return (i, ch.lower())
            i += step
        return (i, "")

    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        
        while i < j:
            i, ch1 = self.find_next_allowed_char(s, i, 1)
            j, ch2 = self.find_next_allowed_char(s, j, -1)
            if ch1 != ch2:
                return False
            i += 1
            j -= 1

        return True
