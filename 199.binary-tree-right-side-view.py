from typing import List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution_one:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        ans: dict[int, int] = {}

        def _rightSideView(node: TreeNode, depth: int = 0) -> None:
            if node.left:
                _rightSideView(node.left, depth + 1)
            if node.right:
                _rightSideView(node.right, depth + 1)
            ans[depth] = node.val

        _rightSideView(root)
        ans = dict(sorted(ans.items()))
        return list(ans.values())


# @leet start


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        ans: list[int] = []
        queue: deque[TreeNode] = deque()
        queue.append(root)

        while queue:
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            ans.append(node.val)

        return ans


# @leet end
