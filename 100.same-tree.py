# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Previous solution - not really good, instead of checking whether the node is None
# just pass the None value to the next call and handle it there!
class Solution_one:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not (p and q):
            return False

        def dfs(node_one: TreeNode, node_two: TreeNode):
            if node_one.val != node_two.val:
                return False

            res_left, res_right = False, False

            if node_one.left is None and node_two.left is None:
                res_left = True
            elif node_one.left and node_two.left:
                res_left = dfs(node_one.left, node_two.left)
            else:
                return False

            if node_one.right is None and node_two.right is None:
                res_right = True
            elif node_one.right and node_two.right:
                res_right = dfs(node_one.right, node_two.right)
            else:
                return False

            return res_left and res_right

        return dfs(p, q)


# @leet start
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# @leet end
