class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        for i,n in enumerate(nums[:-2]):
            if i and n==nums[i-1]:
                continue
            goal=target-nums[i]
            d=set()
            for j in nums[i+1:]:
                if goal-j in d:
                    return target
                else:
                    d.add(j)
        for m in range(1,500):
            for i,n in enumerate(nums[:-2]):
                if i and n==nums[i-1]:
                    continue
                goal=target-nums[i]+m
                d=set()
                for j in nums[i+1:]:
                    if goal-j in d:
                        return target+m
                    else:
                        d.add(j)
            for i,n in enumerate(nums[:-2]):
                if i and n==nums[i-1]:
                    continue
                goal=target-nums[i]-m
                d=set()
                for j in nums[i+1:]:
                    if goal-j in d:
                        return target-m
                    else:
                        d.add(j)