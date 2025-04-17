from __future__ import annotations
from typing import List


class BstNode:
    def __init__(
        self,
        val: int,
        right: BstNode | None = None,
        left: BstNode | None = None,
    ):
        self.val = val
        self.right = right
        self.left = left

    def __str__(self):
        return str(self.val)


class Bst:
    def __init__(self, root: BstNode | None = None):
        self.root = root

    def display(self) -> List[int]:
        ans: List[int] = []

        def _display(node: BstNode | None):
            if node is None:
                return
            _display(node.left)
            ans.append(node.val)
            _display(node.right)

        _display(self.root)
        return ans

    def insert_node(self, new_val: int):
        new_node = BstNode(new_val)
        node: BstNode | None = self.root
        if node is None:
            self.root = new_node
            return

        while node:
            if new_node.val < node.val:
                if not node.left:
                    node.left = new_node
                    return
                node = node.left
            elif new_node.val > node.val:
                if not node.right:
                    node.right = new_node
                    return
                node = node.right
            else:
                # Don't add duplicate nodes (to allow just remove else statement)
                return

    def search(self, data: int) -> bool:
        node: BstNode | None = self.root
        while node:
            if data < node.val:
                node = node.left
            elif data > node.val:
                node = node.right
            else:
                return True
        return False

    def delete_node(self, val: int) -> bool:
        node: BstNode | None = self.root
        parent: BstNode | None = self.root
        while node:
            if val < node.val:
                parent = node
                node = node.left
            elif val > node.val:
                parent = node
                node = node.right
            else:
                break
        if not node:
            return False
        if not node.left and not node.right:
            if parent:
                if parent.left == node:
                    parent.left = None
                elif parent.right == node:
                    parent.right = None
        elif node.left and not node.right:
            parent = node.left
        elif node.right and not node.left:
            parent = node.right
        else:
            tmp_node: BstNode | None = node.right
            if tmp_node and tmp_node.left:
                while tmp_node.left:
                    parent = tmp_node
                    tmp_node = tmp_node.left
                parent.left = None
                node.val = tmp_node.val
            node.val = node.right.val
            node.right = node.right.right

        return True


node1 = BstNode(55)
node2 = BstNode(23)
node3 = BstNode(21)
node4 = BstNode(16)
node5 = BstNode(24)
node6 = BstNode(17)
node7 = BstNode(71)
node8 = BstNode(75)
bst = Bst(node1)
bst.insert_node(node2)
bst.insert_node(node3)
bst.insert_node(node4)
bst.insert_node(node5)
bst.insert_node(node6)
bst.insert_node(node7)
bst.insert_node(node8)

print(bst.display())
print(bst.search(24))
print(bst.delete_node(24))
print(bst.delete_node(55))
print(bst.display())
print(bst.search(24))

