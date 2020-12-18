class Solution:
    def inorderTraversal(self, root):
        res = []
        stack = []
        stack.append(root)
        while len(stack) != 0:
            cur = stack[-1].left
            while cur is not None:
                stack.append(cur)
                cur = cur.left

            elem = stack.pop()
            res.append(elem)
            stack.append(elem.right)

        return res

    def traverse(self, node, order):
        if node is None:
            return
        self.traverse(node.left, order)
        order.append(node.value)
        self.traverse(node.right, order)