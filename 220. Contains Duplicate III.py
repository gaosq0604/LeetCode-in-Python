class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k < 1 or t < 0: return False
        m = len(nums)
        d = {}
        t += 1
        for i in range(m):
            n = nums[i]//t
            if n in d:
                return True
            if n-1 in d and nums[i]-d[n-1] < t:
                return True
            if n+1 in d and d[n+1]-nums[i] < t:
                return True
            d[n] = nums[i]
            if i >= k: d.pop(nums[i-k]//t)
        return False