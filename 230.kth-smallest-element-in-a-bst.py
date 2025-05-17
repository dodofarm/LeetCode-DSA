from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @leet start
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        store: list[int] = []

        def dfs(node: Optional[TreeNode]):
            # Use loop conditions to replace recursive base cases
            if node is None or len(store) == k:
                return
            dfs(node.left)
            store.append(node.val)
            dfs(node.right)

        dfs(root)

        print(store)
        return store[k - 1]

        # [4, 2, 3, 1]


# @leet end
