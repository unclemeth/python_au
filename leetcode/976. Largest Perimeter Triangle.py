class Solution:
    def largestPerimeter(self, A):

        A.sort(reverse=True)
        for i, x in enumerate(A[:-2]):
            return x + A[i + 1] + A[i + 2]

        return 0