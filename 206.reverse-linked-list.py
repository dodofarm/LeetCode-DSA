from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Better because while loop goes till last node! Also easier for type checker
class Solution_one:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        prev = None
        current = head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev  # prev becomes the new head


class Solution_two:
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


class Solution_three:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next

        return prev


# first attempt at recursive solution
class Solution_four:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        new_head = None

        def _reverseList(node: ListNode) -> ListNode:
            nonlocal new_head
            if node.next is None:
                new_head = node
                return node
            prev_node = _reverseList(node.next)
            prev_node.next = node
            return node

        node = _reverseList(head)
        node.next = None
        return new_head


# @leet start


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        new_head = self.reverseList(head.next)
        head.next.next = head
        # Need so that the previous first node will at the end point to None
        head.next = None
        return new_head


# @leet end
