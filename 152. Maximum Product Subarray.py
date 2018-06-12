class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r = imax = imin = nums[0]
        for i in nums[1:]:
            if i < 0:
                imax, imin = imin, imax
            imax = max(i, imax*i)
            imin = min(i, imin*i)
            r = max(r, imax)
        return r