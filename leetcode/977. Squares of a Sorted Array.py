class Solution:
    def sortedSquares(self, nums):
        return sorted([i**2 for i in nums if i > 0][::-1] + [i**2 for i in nums if i <= 0])