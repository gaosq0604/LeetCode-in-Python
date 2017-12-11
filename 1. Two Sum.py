class Solution:
    def twoSum(self, nums, target):
        d = {}
        for i in range(len(nums)):
            m = target - nums[i]
            if m in d:
                return [d[m], i]
            else:
                d[nums[i]] = i
