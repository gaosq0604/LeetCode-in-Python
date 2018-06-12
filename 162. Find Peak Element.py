class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: return 0
        if len(nums) == 2: return 0 if nums[0] > nums[1] else 1
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l+(r-l)//2
            if mid == 0: return mid if nums[mid] > nums[mid+1] else mid+1
            if mid == len(nums)-1: return mid
            if 0< mid < len(nums)-1 and nums[mid-1] < nums[mid] and nums[mid+1] < nums[mid]: return mid
            if nums[mid+1] > nums[mid]:
                l = mid+1
            else:
                r = mid-1