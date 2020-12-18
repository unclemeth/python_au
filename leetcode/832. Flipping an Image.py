class Solution:
    def flipAndInvertImage(self, A):
        return [[1-i for i in row[::-1]] for row in A]