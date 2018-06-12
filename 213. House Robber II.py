class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        if len(nums) <= 3: return max(nums)
        return max(self.rob1(nums[1:]), self.rob1(nums[:-1]))
    
    def rob1(self, nums):
        m = len(nums)
        dp = [0 for _ in range(m+2)]
        for i in range(m):
            dp[i+2] = max(dp[i]+nums[i], dp[i+1])
        return max(dp[-1], dp[-2])