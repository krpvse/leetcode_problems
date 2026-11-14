# 438. Find All Anagrams in a String
# Difficulty: Medium
# Topics: Hash Table, String, Sliding Window
# https://leetcode.com/problems/find-all-anagrams-in-a-string/
#
# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may
# return the answer in any order.
#
# Example 1:
#
# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
#
# Example 2:
#
# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
#
# Constraints:
#
# - 1 <= s.length, p.length <= 3 * 10^4
# - s and p consist of lowercase English letters.

from copy import copy

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        s_qty = len(s)
        p_qty = len(p)
        if p_qty > s_qty:
            return []
        
        res = []

        # Считаем кол-во букв
        letters_qty = p_qty
        counts = dict()
        for l in p:
            if counts.get(l) is None:
                counts[l] = 0 
            counts[l] += 1

        # Создаем стартовое окно
        i = 0
        j = p_qty - 1
        for k in range(i, j+1, 1):
            let = s[k]
            let_counts = counts.get(let)
            if let_counts is not None:
                counts[let] -= 1
                if counts[let] >= 0:
                    letters_qty -= 1
        if letters_qty == 0:
            res.append(i)
        
        # Двигаем окно и ищем анаграммы
        old_let = s[i]
        
        i += 1
        j += 1
        while j < s_qty:
            new_let = s[j]
            
            old_qty = counts.get(old_let)
            if old_qty is not None:
                counts[old_let] += 1
                if counts[old_let] > 0:
                    letters_qty += 1
            new_qty = counts.get(new_let)
            if new_qty is not None:
                counts[new_let] -= 1
                if counts[new_let] >= 0:
                    letters_qty -= 1
            
            if letters_qty == 0:
                res.append(i)
            old_let = s[i]
            i += 1
            j += 1

        return res
