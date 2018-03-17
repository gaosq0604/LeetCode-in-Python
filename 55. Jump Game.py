class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        curmax,lastend=0,0
        while curmax<len(nums)-1:
            lastend,curmax=curmax,max(i+nums[i] for i in range(lastend,curmax+1))
            if lastend==curmax:
                return False
        return True