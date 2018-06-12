class Solution:
    def squaresum(self, n):
        return sum([int(i) ** 2 for i in str(n)])
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = set()
        while n not in s:
            s.add(n)
            n = self.squaresum(n)
        return n == 1