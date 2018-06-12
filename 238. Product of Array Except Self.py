class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = len(nums)
        left = right = 1
        res = [1] * l
        for i in range(l):
            res[i] = left
            left *= nums[i]
        for j in range(l)[::-1]:
            res[j] *= right
            right *= nums[j]      
        return res