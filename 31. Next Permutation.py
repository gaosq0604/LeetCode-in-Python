class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range (len(nums)-2,-1,-1):
            for j in range (len(nums)-1,i,-1):
                if nums[i]<nums[j]:
                    nums[i],nums[j]=nums[j],nums[i]
                    m=i+1
                    n=len(nums)-1
                    while m<n:
                        nums[m],nums[n]=nums[n],nums[m]
                        m+=1
                        n-=1
                    return
        nums.reverse()
        return