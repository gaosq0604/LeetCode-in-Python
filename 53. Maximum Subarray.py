class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cursum=maxsum=nums[0]
        for num in nums[1:]:
            cursum=max(num,cursum+num)
            maxsum=max(cursum,maxsum)
        return maxsum