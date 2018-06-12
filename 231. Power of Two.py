class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        '''if n <= 0: return False
        while n > 1:
            n, r = divmod(n, 2)
            if r: return False
        return True'''
    
        return n > 0 and not (n & n-1)