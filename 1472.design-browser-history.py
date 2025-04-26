from __future__ import annotations


# @leet start
class HistoryNode:
    def __init__(
        self,
        url: str,
        # disabled due to LC not working with annotations
        # prev: HistoryNode | None = None,
        # next: HistoryNode | None = None,
        prev=None,
        next=None,
    ):
        self.url = url
        self.prev = prev
        self.next = next

    def __str__(self):
        output = [self.url]
        next = self.next
        while next:
            output.append(next.url)
            next = next.next

        return str(output)


class BrowserHistory:
    def __init__(self, homepage: str):
        self.curr = HistoryNode(homepage)

    def visit(self, url: str) -> None:
        self.curr.next = HistoryNode(url, self.curr)
        self.curr = self.curr.next

    def back(self, steps: int) -> str:
        node = self.curr
        while node.prev and steps != 0:
            node = node.prev
            steps -= 1

        self.curr = node
        return self.curr.url

    def forward(self, steps: int) -> str:
        node = self.curr
        while node.next and steps != 0:
            node = node.next
            steps -= 1

        self.curr = node
        return self.curr.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
# @leet end
