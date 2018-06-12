class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = []
        while n:
            res.append(chr((n-1)%26+ord('A')))
            n = (n-1)//26
        return ''.join(reversed(res))