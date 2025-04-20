# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# @leet start
class Solution:
    def reorderList(self, head: ListNode) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half
        current = slow.next
        slow.next = None
        prev = None
        # print(current)
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        # Merge the two halves

        p1, p2 = head, prev
        while p2:
            p1_next = p1.next
            p2_next = p2.next

            p1.next = p2
            p2.next = p1_next

            p1 = p1_next
            p2 = p2_next


# @leet end
