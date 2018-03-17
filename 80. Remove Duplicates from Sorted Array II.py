class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        '''while i<len(nums)-1:
            if nums[i]==nums[i+1]:
                tmp=nums[i]
                while i<len(nums)-2 and nums[i+2]==tmp:
                    nums.pop(i+2)
            i+=1
        return len(nums)'''
        for num in nums:
            if i<2 or num>nums[i-2]:
                nums[i]=num
                i+=1
        return i