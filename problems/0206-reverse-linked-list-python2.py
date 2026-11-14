# 206. Reverse Linked List
# Difficulty: Easy
# Topics: Linked List, Recursion
# https://leetcode.com/problems/reverse-linked-list/
#
# Given the head of a singly linked list, reverse the list, and return the reversed list.
#
# Example 1:
#
# [image: https://assets.leetcode.com/uploads/2021/02/19/rev1ex1.jpg]
#
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
#
# Example 2:
#
# [image: https://assets.leetcode.com/uploads/2021/02/19/rev1ex2.jpg]
#
# Input: head = [1,2]
# Output: [2,1]
#
# Example 3:
#
# Input: head = []
# Output: []
#
# Constraints:
#
# - The number of nodes in the list is the range [0, 5000].
# - -5000 <= Node.val <= 5000
#
# Follow up: A linked list can be reversed either iteratively or recursively. Could you implement
# both?

class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return head
        
        previous_node = head
        current_node = head.next
        head.next = None
        while True:
            remembered_node = current_node.next
            
            current_node.next = previous_node

            if remembered_node is not None:
                previous_node = current_node
                current_node = remembered_node
            else:
                head = current_node
                break
        
        return head
