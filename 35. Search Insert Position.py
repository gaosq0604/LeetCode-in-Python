class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l,r=0,len(nums)-1
        while l<=r:
            m=(l+r)//2
            if nums[m]>=target:
                r=m-1
            else:
                l=m+1
        return l