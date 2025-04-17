from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @leet start
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        ans: List[List[int]] = []

        def _levelOrder(node: TreeNode, depth=-1):
            depth += 1
            if len(ans) - 1 < depth:
                ans.append([])
            if node.left:
                _levelOrder(node.left, depth)
            if node.right:
                _levelOrder(node.right, depth)

            ans[depth].append(node.val)

        _levelOrder(root)
        return ans


# @leet end

