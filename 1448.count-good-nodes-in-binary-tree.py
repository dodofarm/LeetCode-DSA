# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursive Solution - doesn't look elegant, the last one does!
class Solution_one:
    def goodNodes(self, root: TreeNode) -> int:
        def _goodNodes(node: TreeNode, max_value: int) -> int:
            max_value = max(max_value, node.val)
            left = _goodNodes(node.left, max_value) if node.left else 0
            right = _goodNodes(node.right, max_value) if node.right else 0
            return left + right + 1 if node.val >= max_value else left + right

        return _goodNodes(root, root.val)


class Solution_two:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        stack: list[tuple[TreeNode, int]] = [(root, root.val)]
        while stack:
            node, value = stack.pop()
            value = max(value, node.val)
            if node.right:
                stack.append((node.right, value))
            if node.left:
                stack.append((node.left, value))
            if node.val >= value:
                ans += 1
        return ans


# @leet start


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, max_path) -> int:
            ans = 0
            if node.val >= max_path:
                ans += 1
            max_path = max(max_path, node.val)
            if node.left:
                ans += dfs(node.left, max_path)
            if node.right:
                ans += dfs(node.right, max_path)
            return ans

        return dfs(root, root.val)


# @leet end
