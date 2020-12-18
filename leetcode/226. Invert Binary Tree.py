class Solution:
    def invertTree(self, root):
        return self.invert(root)

    def invert(self, node):
        if node is None:
            return
        node.left, node.right = node.right, node.left
        self.invert(node.left)
        self.invert(node.right)
        return node