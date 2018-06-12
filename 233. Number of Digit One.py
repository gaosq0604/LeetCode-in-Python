class Solution:
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        q, x, res = n, 1, 0
        while q > 0:
            q, digit = divmod(q, 10)
            res += q * x
            if digit == 1:
                res += n % x + 1
            elif digit > 1:
                res += x
            x *= 10
        return res