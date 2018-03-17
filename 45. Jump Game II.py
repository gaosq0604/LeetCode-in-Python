class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        step,curmax,lastend=0,0,0
        while curmax<len(nums)-1:
            step+=1
            lastend,curmax=curmax+1,max(i+nums[i] for i in range(lastend,curmax+1))
        return step