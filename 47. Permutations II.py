class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        self.res=[]
        self.dfs(nums,[])
        return list(self.res)
    def dfs(self,nums,path):
        if not nums:
            self.res.append(path)
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            self.dfs(nums[:i]+nums[i+1:],path+[nums[i]])
        '''res=[[]]
        for n in nums:
            newres=[]
            for item in res:
                for i in range(len(item)+1):
                    newres.append(item[:i]+[n]+item[i:])
                    if i<len(item) and item[i]==n:
                        break
            res=newres
        return res'''