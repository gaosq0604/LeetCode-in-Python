class Solution:
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2: return 0
        nums = self.radixSort(nums)
        res = 0
        for i in range(1, len(nums)):
            res = max(nums[i] - nums[i - 1], res)
        return res
    
    def radixSort(self, nums):
        for i in range(31):
            onebucket = []
            zerobucket = []
            needle = 1 << i
            for j in range(len(nums)):
                if nums[j] & needle != 0:
                    onebucket.append(nums[j])
                else:
                    zerobucket.append(nums[j])
            nums = []
            nums += zerobucket
            nums += onebucket
        return nums