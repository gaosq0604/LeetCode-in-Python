class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        i = 0
        while i < len(nums)-1:
            start = i
            while i < len(nums)-1 and nums[i+1] == nums[i]+1:
                i += 1
            if i > start:
                res.append("{}->{}".format(nums[start], nums[i]))
            else:
                res.append(str(nums[i]))
            i += 1
        if i < len(nums):
            res.append(str(nums[i]))
        return res