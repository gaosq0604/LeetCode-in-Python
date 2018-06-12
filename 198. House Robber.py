class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = len(nums)
        dp = [0 for _ in range(m+2)]
        for i in range(m):
            dp[i+2] = max(dp[i]+nums[i], dp[i+1])
        return max(dp[-1], dp[-2])