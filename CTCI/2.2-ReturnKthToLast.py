class Node:
    def __init__(self):
        self.next = None
        self.data = 0


# Implement an algorithm to find the kth to last element of a singly linked list.


def nth_element_print(head: Node, k: int) -> int:
    if head.next is None:
        return 1
    node_num = nth_element_print(head.next, k)
    if k == node_num:
        print(head)
        return node_num + 1
    else:
        return node_num + 1


def nth_element_two_pointer(head: Node, k: int) -> Node:
    p1 = head
    p2 = head

    for i in range(k):
        p2 = p2.next

    while p2:
        p1 = p1.next
        p2 = p2.next

    return p1
