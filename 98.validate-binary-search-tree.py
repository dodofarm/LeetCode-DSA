from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @leet start
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def _isValidBST(node, min_value, max_value) -> bool:
            if node is None:
                return True

            if not min_value < node.val < max_value:
                return False
            left = _isValidBST(node.left, min_value, node.val)
            right = _isValidBST(node.right, node.val, max_value)
            return left and right

        return _isValidBST(root, float("-inf"), float("+inf"))


# @leet end
