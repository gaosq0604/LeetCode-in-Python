class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length=len(nums)
        #res=[]
        '''for i in range(len(nums)+1):
            for j in itertools.combinations(nums,i):
                res.append(list(j))
        return res'''
        '''def dfs(index,path):
            res.append(path)
            for i in range(index,length):
                dfs(i+1,path+[nums[i]])
        dfs(0,[])
        return res'''
        res=[[]]
        for num in nums:
            res+=[item+[num] for item in res]
        return res