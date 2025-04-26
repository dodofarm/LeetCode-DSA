# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# @leet start
class Solution:
    def createPath(self, root: TreeNode, node: TreeNode) -> list[TreeNode]:
        path: list[TreeNode] = []
        while root:
            if node.val > root.val:
                path.append(root)
                root = root.right
            elif node.val < root.val:
                path.append(root)
                root = root.left
            else:
                path.append(root)
                break
        return path

    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        path_p = self.createPath(root, p)
        path_q = self.createPath(root, q)

        length = min(len(path_p), len(path_q))
        node_p, node_q = 0, 0
        for _ in range(length):
            if path_p[node_p] is not path_q[node_q]:
                return path_p[node_p - 1]
            node_p += 1
            node_q += 1

        if node_p == len(path_p):
            return path_p[node_p - 1]

        if node_q == len(path_q):
            return path_q[node_q - 1]

        return TreeNode(0)


# @leet end
