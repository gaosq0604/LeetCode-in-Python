class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = {}
        for item in nums:
            if item in d:
                return True
            d[item] = 1
        return False