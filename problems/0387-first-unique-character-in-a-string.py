# 387. First Unique Character in a String
# Difficulty: Easy
# Topics: Hash Table, String, Queue, Counting
# https://leetcode.com/problems/first-unique-character-in-a-string/
#
# Given a string s, find the first non-repeating character in it and return its index. If it does not
# exist, return -1.
#
# Example 1:
#
# Input: s = "leetcode"
#
# Output: 0
#
# Explanation:
#
# The character 'l' at index 0 is the first character that does not occur at any other index.
#
# Example 2:
#
# Input: s = "loveleetcode"
#
# Output: 2
#
# Example 3:
#
# Input: s = "aabb"
#
# Output: -1
#
# Constraints:
#
# - 1 <= s.length <= 10^5
# - s consists of only lowercase English letters.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s) == 1:
            return 0
        
        qty = len(s)

        checked = set()

        i = 0
        while i < qty:
            if s[i] not in checked:
                if i == qty - 1:
                    return i
                
                j = i + 1
                if j < qty:
                    uniq = True
                    while j < qty:
                        if s[i] == s[j]:
                            checked.add(s[i])
                            uniq = False
                            break
                        j += 1
                    if uniq:
                        return i
            i += 1

        return -1
