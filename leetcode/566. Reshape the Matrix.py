class Solution:
    def matrixReshape(self, nums, r, c) :
        return nums if len(sum(nums, [])) != r * c else map(list, zip(*([iter(sum(nums, []))]*c)))