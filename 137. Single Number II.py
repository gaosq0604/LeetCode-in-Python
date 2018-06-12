class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numlen = len(nums)
        res = 0
        for i in range(32):
            sum = 0
            for j in range(numlen):
                sum += nums[j] >> i & 1
            res |= (sum % 3) << i;
        return res
        '''a= set(nums)
        a = sum(a)*3 -sum(nums)
        a = a//2
        return a'''