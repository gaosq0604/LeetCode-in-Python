class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        '''if not nums:
            return []
        ans = []
        prev_max = max(nums[:k])
        ans.append(prev_max)
        for i in range(k,len(nums)):
            if nums[i] > prev_max:
                prev_max = nums[i]
            elif nums[i-k] == prev_max:
                prev_max = max(nums[i-k+1:i+1])
            ans.append(prev_max)
        return ans '''
        from collections import deque
        deq = deque()
        result = []
        for i, num in enumerate(nums):
            if deq and i - deq[0][1] == k:
                deq.popleft()
            while deq and num >= deq[-1][0]:
                deq.pop()
            deq.append((num, i))
            if i >= k - 1:
                result.append(deq[0][0])
        return result