class Solution(object):
    def rob(self, nums):
        if len(nums)==0: return 0
        elif len(nums)==1: return nums[0]
        else:
            max_arr = [0]*(len(nums))
            max_arr[0] = nums[0]
            max_arr[1] = max(nums[0],nums[1])
            for i in range(2,len(nums)):
                max_arr[i] = max(max_arr[i-2]+nums[i], max_arr[i-1])

            return max_arr[-1]