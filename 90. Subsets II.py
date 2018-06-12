class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[[]]
        nums.sort()
        for i,num in enumerate(nums):
            if i==0 or num!=nums[i-1]:
                l=len(res)
            for item in res[len(res)-l:]:
                res+=[item+[num]]
            #res+=[item+[num] for item in res if item+[num] not in res]
        return res