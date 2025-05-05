from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @leet start
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        def _isBalanced(node: Optional[TreeNode]) -> tuple[bool, int]:
            if node is None:
                return (True, 0)

            node_left_valid, node_left_depth = _isBalanced(node.left)
            node_right_valid, node_right_depth = _isBalanced(node.right)

            difference = abs(node_left_depth - node_right_depth)
            # print(node.val, difference, node_left_depth, node_right_depth)

            return (
                difference <= 1 if node_left_valid and node_right_valid else False,
                max(node_left_depth, node_right_depth) + 1,
            )

        return _isBalanced(root)[0]


# @leet end
