class Solution:
    def kthSmallest(self, root, k):
        i = 0
        stack = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            i += 1
            if i == k:
                return node.val
            node = node.right