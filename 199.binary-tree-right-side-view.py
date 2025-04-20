from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @leet start
class Solution:
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


# @leet end
