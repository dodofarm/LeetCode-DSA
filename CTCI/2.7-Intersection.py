# Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the
# intersecting node. Note that the intersection is defined based on reference, not value. That is, if the
# kth node of the first linked list is the exact same node (by reference) as the jth node of the second
# linked list, then they are intersecting.


class Node:
    def __init__(self, next=None, data=0):
        self.next = next
        self.data = data


def find_intersection(head_one: Node, head_two: Node) -> Node:
    length_one = linked_list_length(head_one)
    length_two = linked_list_length(head_two)

    if length_one > length_two:
        difference = length_one - length_two
        for i in range(0, difference):
            head_one = head_one.next

    if length_one < length_two:
        difference = length_two - length_one
        for i in range(0, difference):
            head_two = head_two.next

    while head_one != head_two:
        head_one = head_one.next
        head_two = head_two.next

    return head_one


def linked_list_length(head: Node) -> int:
    node = head
    count = 0
    while node:
        count += 1
        node = node.next

    return count
