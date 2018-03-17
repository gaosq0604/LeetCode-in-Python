class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i,j,k=0,len(nums)-1,0
        while k<=j:
            while nums[k]==2 and k<=j:
                nums[k],nums[j]=nums[j],nums[k]
                j-=1
            while nums[k]==0 and k>=i:
                nums[k],nums[i]=nums[i],nums[k]
                i+=1
            k+=1