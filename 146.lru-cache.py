from typing import Optional


# @leet start
class Node:
    def __init__(
        self,
        key: int,
        val: int,
        next: "Optional[Node]" = None,
        prev: "Optional[Node]" = None,
    ):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

    def __str__(self) -> str:
        return f"{self.key, self.val}"


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache: dict[int, Node] = {}
        self.head = Node(-1, 0)
        self.tail = Node(99, 99)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.length = 0

    def _insert_node(self, node: Node, new_node: Node):
        new_node.next, new_node.prev = node.next, node
        node.next.prev = new_node
        node.next = new_node
        print(f"Insert node, Prev node: {new_node.prev}")
        print(f"Insert node, Next node: {new_node.next}")

    def _remove_node(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev
        print(f"Remove node, Prev node: {node.prev}")
        print(f"Remove node, Next node: {node.next}")

    def get(self, key: int) -> int:
        if key in self.cache:
            print(f"Moving up in cache, {self.cache[key]}")
            self._remove_node(self.cache[key])
            self._insert_node(self.head, self.cache[key])
            print(f"VALUE TO BE RETURNED: {self.cache[key].val}")
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        print(f"{self.length = }")
        if key in self.cache:
            print(f"Updating {self.cache[key]}")
            self._remove_node(self.cache[key])
            self.length -= 1
        if self.length >= self.capacity:
            print("Capacity reached")
            print(f"Deleting: {self.tail.prev}")
            self.cache.pop(self.tail.prev.key)
            self._remove_node(self.tail.prev)
            self.length -= 1

        new_node = Node(key, value)
        self.cache[key] = new_node
        print(f"Inserted: { key = }, {value = }")
        self._insert_node(self.head, new_node)
        self.length += 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @leet end
