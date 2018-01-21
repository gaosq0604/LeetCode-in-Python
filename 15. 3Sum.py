class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        s=set()
        nums.sort()
        for i,n in enumerate(nums[:-2]):
            if n>0:
                break
            if i and n==nums[i-1]:
                continue
            goal=-nums[i]
            d=set()
            for j in nums[i+1:]:
                if goal-j in d:
                    if j<goal-j:
                        break
                    s.add((n,goal-j,j))
                else:
                    d.add(j)
        return list(s)