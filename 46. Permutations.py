class Solution:
    res=[]
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res=[]
        self.dfs(nums,[])
        return self.res
    def dfs(self,nums,path):
        if not nums:
            self.res.append(path)
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:],path+[nums[i]])
        #return [[n]+p for i,n in enumerate(nums) for p in self.permute(nums[:i]+nums[i+1:]) or [[]]]