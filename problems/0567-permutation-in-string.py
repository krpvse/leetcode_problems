# 567. Permutation in String
# Difficulty: Medium
# Topics: Hash Table, Two Pointers, String, Sliding Window
# https://leetcode.com/problems/permutation-in-string/
#
# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
#
# In other words, return true if one of s1's permutations is the substring of s2.
#
# Example 1:
#
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
#
# Example 2:
#
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
#
# Constraints:
#
# - 1 <= s1.length, s2.length <= 10^4
# - s1 and s2 consist of lowercase English letters.

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        qty1 = len(s1)
        qty2 = len(s2)
        if qty2 < qty1:
            return False

        # Формируем счетчики
        counter = qty1
        letters = dict()
        for let in s1:
            if not letters.get(let):
                letters[let] = 0
            letters[let] += 1

        # Ставим первичное окно
        i = 0
        j = 0
        while True:
            let = s2[j]
            let_counts = letters.get(let)
            if let_counts is not None:
                if let_counts > 0:
                    counter -= 1
                letters[let] -= 1
            
            if j == qty1 - 1:
                break
            
            j += 1
        
        if counter == 0:
            return True

        # Двигаем окно
        old_let = s2[i]
        i += 1
        j += 1
        while j < qty2:
            let_counts = letters.get(old_let)
            if let_counts is not None:
                if let_counts >= 0:
                    counter += 1
                letters[old_let] += 1
            
            new_let = s2[j]
            let_counts = letters.get(new_let)
            if let_counts is not None:
                if let_counts > 0:
                    counter -= 1
                letters[new_let] -= 1
            
            if counter == 0:
                return True
            
            old_let = s2[i]
            i += 1
            j += 1

        return False
