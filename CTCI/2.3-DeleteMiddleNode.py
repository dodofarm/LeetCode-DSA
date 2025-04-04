class Node:
    def __init__(self):
        self.next = None
        self.data = 0


# Implement an algorithm to delete a node in the middle (i.e., any node but
# the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
# that node.
# EXAMPLE
# lnput:the node c from the linked list a->b->c->d->e->f
# Result: nothing is returned, but the new linked list looks like a->b->d->e->f


def delete_middle_node(head: Node) -> bool:
    if head.next is None or head is None:
        return False

    head.data = head.next.data
    head.next = head.next.next
    return True
