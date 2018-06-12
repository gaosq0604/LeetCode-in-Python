class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        l, length, cur = 0, float('inf'), 0
        for r, num in enumerate(nums):
            cur += num
            while cur >= s:
                length, l, cur = min(length, r-l+1), l+1, cur-nums[l]
        return length <= len(nums) and length or 0