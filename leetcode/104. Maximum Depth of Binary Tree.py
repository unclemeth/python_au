class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        else:
            leftN = self.maxDepth(root.left)
            rightN = self.maxDepth(root.right)
            return max(leftN,rightN)+1