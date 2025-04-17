from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @leet start
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        def _invertTree(node: TreeNode):
            if node.left:
                _invertTree(node.left)

            if node.right:
                _invertTree(node.right)
            # technically this can be removed if you're fine with swapping None with None
            if node.left or node.right:
                node.left, node.right = node.right, node.left

        _invertTree(root)

        return root


# @leet end

