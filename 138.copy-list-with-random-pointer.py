from typing import Optional


# Definition for a Node.
class Node:
    def __init__(
        self, x: int, next: "Optional[Node]" = None, random: "Optional[Node]" = None
    ):
        self.val = int(x)
        self.next = next
        self.random = random


# @leet start


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if head is None:
            return None

        pairs: dict[Node, Node] = {}
        node: Optional[Node] = head
        while node:
            print(node.val)
            pairs[node] = Node(node.val)
            node = node.next

        for old_node, new_node in pairs.items():
            new_node.next = pairs[old_node.next] if old_node.next else None
            new_node.random = pairs[old_node.random] if old_node.random else None

        return pairs[head]


# @leet end
