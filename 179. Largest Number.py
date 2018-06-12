class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        from functools import cmp_to_key
        nums = [str(x) for x in nums]
        nums.sort(key = cmp_to_key(lambda x, y: int(y+x)-int(x+y)))
        return ''.join(nums).lstrip('0') or '0'