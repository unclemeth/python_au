def isSymmetricBst(node1, node2):
    if node1 == None and node2 == None:
        return True
    elif node1 == None or node2 == None:
        return False
    else:
        return node1.val == node2.val and isSymmetricBst(node1.left, node2.right) and isSymmetricBst(node1.right,
                                                                                                     node2.left)


class Solution:
    def isSymmetric(self, root):
        if not root:
            return True
        return isSymmetricBst(root.left, root.right)