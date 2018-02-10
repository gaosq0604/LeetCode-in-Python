class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=len(nums)
        if not l:
            return 0
        count=1
        for i in range(1,l):
            if nums[i]!=nums[i-1]:
                nums[count]=nums[i]
                count+=1
        return count