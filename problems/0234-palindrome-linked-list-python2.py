# 234. Palindrome Linked List
# Difficulty: Easy
# Topics: Linked List, Two Pointers, Stack, Recursion
# https://leetcode.com/problems/palindrome-linked-list/
#
# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
#
# Example 1:
#
# [image: https://assets.leetcode.com/uploads/2021/03/03/pal1linked-list.jpg]
#
# Input: head = [1,2,2,1]
# Output: true
#
# Example 2:
#
# [image: https://assets.leetcode.com/uploads/2021/03/03/pal2linked-list.jpg]
#
# Input: head = [1,2]
# Output: false
#
# Constraints:
#
# - The number of nodes in the list is in the range [1, 10^5].
# - 0 <= Node.val <= 9
#
# Follow up: Could you do it in O(n) time and O(1) space?

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        
        l = []

        node = head
        l.append(node.val)
        while node.next:
            node = node.next
            l.append(node.val)
        
        i = 0
        j = len(l) - 1

        while i < j:
            if l[i] != l[j]:
                return False
            i += 1
            j -= 1
        
        return True
