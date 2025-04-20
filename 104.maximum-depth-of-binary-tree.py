from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# recursive Solution, the iterative one basically replicates the call stack
class Solution_one:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left = 0
        right = 0
        if root.left:
            left = self.maxDepth(root.left)
        if root.right:
            right = self.maxDepth(root.right)

        return max(left, right) + 1
        # could also do oneliner:
        # return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


# @leet start
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        ans = 1
        stack = [(root, ans)]

        while stack:
            node, depth = stack.pop()
            if node.right:
                stack.append((node.right, depth + 1))

            if node.left:
                stack.append((node.left, depth + 1))

            ans = max(depth, ans)

        return ans


# @leet end
