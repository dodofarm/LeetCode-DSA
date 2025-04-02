class Node:
    def __init__(self):
        self.next = None
        self.data = 0


# Write code to remove duplicates from an unsorted linked list.
def remove_duplicates(head: Node):
    node = head
    if not head:
        return head

    data = set()
    prev_node = node
    while node:
        if node.data in data:
            prev_node.next = node.next
        else:
            data.add(node.data)
            prev_node = node

        node = node.next


# Follow up:
# How would you solve this problem if a temporary buffer is not allowed
def remove_duplicates_no_buffer(head: Node):
    current_node = Node()
    while current_node:
        node = current_node.next
        prev_node = current_node
        while node:
            if current_node.data == node.data:
                prev_node.next = node.next
            else:
                prev_node = node

            node = node.next

        current_node = current_node.next
