class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        numlen=len(nums)
        #s=set()
        d=[]
        nums.sort()
        for i,n in enumerate(nums[:-3]):
            if n>target/4:
                break
            if i and n==nums[i-1]:
                continue
            for j in range(i+1,numlen-2):
                target2=target-n
                if nums[j]>target2/3:
                    break
                if j-i-1 and nums[j]==nums[j-1]:
                    continue
                goal=target2-nums[j]
                k=j+1
                l=numlen-1
                if nums[k]>goal/2 or nums[l]<goal/2:
                    continue
                while k<l:
                    sum2=nums[k]+nums[l]
                    if sum2==goal:
                        d.append([n,nums[j],nums[k],nums[l]])
                        k+=1
                        while k<l and nums[k]==nums[k-1]:
                            k+=1
                        l-=1
                        while k<l and nums[l]==nums[l+1]:
                            l-=1
                    elif sum2<goal:
                        k+=1
                    else:
                        l-=1
        return d
        '''def findNsum(nums, target, N, result, results):
            if len(nums) < N or N < 2 or target < nums[0]*N or target > nums[-1]*N:  # early termination
                return
            if N == 2:
                l,r = 0,len(nums)-1
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else: # recursively reduce N
                for i in range(len(nums)-N+1):
                    if i == 0 or (i > 0 and nums[i-1] != nums[i]):
                        findNsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)

        results = []
        findNsum(sorted(nums), target, 4, [], results)
        return results'''