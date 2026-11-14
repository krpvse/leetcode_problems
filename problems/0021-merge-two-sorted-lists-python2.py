# 21. Merge Two Sorted Lists
# Difficulty: Easy
# Topics: Linked List, Recursion
# https://leetcode.com/problems/merge-two-sorted-lists/
#
# You are given the heads of two sorted linked lists list1 and list2.
#
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of
# the first two lists.
#
# Return the head of the merged linked list.
#
# Example 1:
#
# [image: https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg]
#
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
#
# Example 2:
#
# Input: list1 = [], list2 = []
# Output: []
#
# Example 3:
#
# Input: list1 = [], list2 = [0]
# Output: [0]
#
# Constraints:
#
# - The number of nodes in both lists is in the range [0, 50].
# - -100 <= Node.val <= 100
# - Both list1 and list2 are sorted in non-decreasing order.

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        i = list1
        j = list2
        if not i and not j:
            return i
        elif not i:
            return j
        elif not j:
            return i

        # Определение первой ноды
        if i.val < j.val:
            head = i
            i = i.next
        else:
            head = j
            j = j.next

        # Объединение списков
        node = head
        while True:
            if not i and not j:
                break
            elif not i:
                node.next = j
                break
            elif not j:
                node.next = i
                break
            elif i.val < j.val:
                node.next = i
                i = i.next
                node = node.next
            else:
                node.next = j
                j = j.next
                node = node.next
            
        return head
