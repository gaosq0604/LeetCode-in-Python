class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l,r=0,len(height)-1
        if r<0:
            return 0
        s=0
        minh=min(height[l],height[r])
        while l<r:
            while l<r and height[l]<=minh:
                s+=minh-height[l]
                l+=1
            while l<r and height[r]<=minh:
                s+=minh-height[r]
                r-=1
            minh=min(height[l],height[r])
        return s
            