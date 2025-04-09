from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Better and correct because whle lioop goes till last node! Also easier for type checker
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head:
#             return None
#
#         prev = None
#         current = head
#
#         while current:
#             next_node = current.next
#             current.next = prev
#             prev = current
#             current = next_node
#
#         return prev  # prev becomes the new head


# @leet start
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        prev = None
        while head.next is not None:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node

        head.next = prev
        return head


# @leet end

