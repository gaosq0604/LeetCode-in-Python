class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1,-1]
        n=len(nums)-1
        if n==0:
            if nums[0]==target:
                return [0,0]
            else:
                return [-1,-1]
        l,r=0,n
        while l<r:
            mid=(l+r)//2
            if nums[mid]<target:
                l=mid+1
            else:
                r=mid
        if nums[l]!=target:
            return [-1,-1]
        left,r=l,n
        while l<r:
            mid=(l+r)//2+1
            if nums[mid]>target:
                r=mid-1
            else:
                l=mid
        return [left,r]