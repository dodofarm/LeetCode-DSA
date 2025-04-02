# Sum Lists: You have two numbers represented by a linked list, where each node contains a single
# digit. The digits are stored in reverse order,such that the 1's digit is at the head of the list. Write a
# function that adds the two numbers and returns the sum as a linked list.
# EXAMPLE
# Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295.
# Output: 2 -> 1 -> 9. That is,912.
# FOLLOW UP
# Suppose the digits are stored in forward order. Repeat the above problem.
# Input: (6 -> 1 -> 7) + (2 -> 9 -> 5).That is,617 + 295.
# Output: 9 -> 1 -> 2.That is, 912.


class Node:
    def __init__(self, next=None, data=0):
        self.next = next
        self.data = data


def reverse_sum_linked_list(head: Node) -> int:
    if head.next is None:
        return head.data
    return int(str(reverse_sum_linked_list(head.next)) + str(head.data))


def sum_lists(head_one: Node, head_two: Node) -> Node:
    sum = list(
        reversed(
            str(reverse_sum_linked_list(head_one) + reverse_sum_linked_list(head_two))
        )
    )
    head = Node(sum.pop(0))
    node = head
    for i in sum:
        next = Node(data=i)
        node.next = next
        node = node.next
    return head
