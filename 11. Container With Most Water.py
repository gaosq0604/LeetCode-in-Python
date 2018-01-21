class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        s=0
        low,high=0,len(height)-1
        while low<high:
            if height[low]<height[high]:
                s=max(s,height[low]*(high-low))
                low+=1
            else:
                s=max(s,height[high]*(high-low))
                high-=1
        return s