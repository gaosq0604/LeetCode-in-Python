class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums)-1
        while r > l:
            m = l+(r-l)//2
            if nums[m] > nums[r]:
                l = m+1
            elif nums[m] < nums[r]:
                r = m
            elif nums[l] < nums[r]:
                r = m
            else:
                l += 1
        return nums[l]