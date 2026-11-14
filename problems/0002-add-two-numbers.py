# 2. Add Two Numbers
# Difficulty: Medium
# Topics: Linked List, Math, Recursion
# https://leetcode.com/problems/add-two-numbers/
#
# You are given two non-empty linked lists representing two non-negative integers. The digits are
# stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and
# return the sum as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example 1:
#
# [image: https://assets.leetcode.com/uploads/2020/10/02/addtwonumber1.jpg]
#
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
#
# Example 2:
#
# Input: l1 = [0], l2 = [0]
# Output: [0]
#
# Example 3:
#
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
#
# Constraints:
#
# - The number of nodes in each linked list is in the range [1, 100].
# - 0 <= Node.val <= 9
# - It is guaranteed that the list represents a number that does not have leading zeros.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_str = ""
        i = l1
        while i is not None:
            l1_str = str(i.val) + l1_str
            i = i.next
        if not l1_str:
            return l2

        l2_str = ""
        i = l2
        while i is not None:
            l2_str = str(i.val) + l2_str
            i = i.next
        if not l2_str:
            return l1

        l_sum = str(int(l1_str) + int(l2_str))

        head = ListNode(val=int(l_sum[-1]), next=None)
        node = head
        for i in range(len(l_sum)-2, -1, -1):
            digit = int(l_sum[i])
            node.next = ListNode(val=digit, next=None)
            node = node.next

        return head
