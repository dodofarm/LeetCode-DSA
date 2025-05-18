# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @leet start
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        res = 0

        def max_depth(node: TreeNode) -> int:
            nonlocal res
            if node is None:
                return 0
            left, right = max_depth(node.left), max_depth(node.right)
            res = max(res, left + right)

            return max(left, right) + 1

        max_depth(root)
        return res


# @leet end
