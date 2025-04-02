from typing import Optional


class Node:
    def __init__(self):
        self.next = None
        self.data = 0


# Write code to partition a linked list around a value x, such that all nodes less than x come
# before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
# to be after the elements less than x (see below). The partition element x can appear anywhere in the
# "right partition"; it does not need to appear between the left and right partitions.
# EXAMPLE
# Input:
# Output:
# 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition= 5]
# 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8


# Solution that keeps initial order of the list in tact
def partition_linked_list(head: Node, partition: int) -> bool | Node:
    if head is None or head.next is None:
        return False

    startPrePart: Optional[Node] = None
    prePart: Optional[Node] = None
    startPostPart: Optional[Node] = None
    postPart: Optional[Node] = None
    node = head
    while node:
        next = node.next
        if node.data < partition:
            if not startPrePart:
                startPrePart = node
                prePart = node
            elif prePart:
                prePart.next = node
                prePart = node
        else:
            if not startPostPart:
                startPostPart = node
                postPart = node
            elif postPart:
                postPart.next = node
                postPart = node
        node = next

    if postPart:
        postPart.next = None

    if prePart:
        prePart.next = startPostPart

    result = startPrePart if startPrePart else startPostPart
    assert result is not None
    return result


# Solution that generates the finished linked list directly, space complexity O(1)
def partition_unordered(head: Node, partition: int) -> bool | Node:
    if head is None or head.next is None:
        return False

    head = head
    tail = head

    node = head
    while node:
        next = node.next
        if node.data < partition:
            node.next = head
            head = node
        else:
            tail.next = node
            tail = node

        node = next

    tail.next = None
    return head
