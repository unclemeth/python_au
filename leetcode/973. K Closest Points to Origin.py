from math import sqrt


class Solution():
    def kClosest(self, points, K):
        return sorted(points, key = lambda p : sqrt(p[0] * p[0] + p[1] * p[1]))[:K]