from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# @leet start
# Definition for singly-linked list.
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return head

        slow, fast = head, head

        for i in range(n):
            fast = fast.next

        if fast is None:
            return slow.next

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return head


# @leet end

