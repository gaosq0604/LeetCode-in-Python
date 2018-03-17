class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append(0)
        n=len(nums)
        for i in range(n):
            if nums[i]>=n or nums[i]<0:
                nums[i]=0
        for i in nums:
            if i>0:
                nums[i%n]+=n
        for i in range(1,n):
            if nums[i]<n:
                return i
        return n