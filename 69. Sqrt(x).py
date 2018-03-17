class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        i=x
        while i*i>x:
            i=(i+x//i)//2
        return i