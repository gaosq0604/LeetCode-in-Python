class Solution:
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        sign = '-' if numerator * denominator < 0 else ''
        numerator, denominator = abs(numerator), abs(denominator)
        a, b = divmod(numerator, denominator)
        if b == 0:
            return sign + str(numerator//denominator)
        res = [sign+str(a), '.']
        seen = {}
        i = 2
        while b:
            if b in seen:
                return "".join(res[:seen[b]]) + "(" + "".join(res[seen[b]:]) + ")"
            seen[b] = i
            a, b = a, b = divmod(b*10, denominator)
            res.append(str(a))
            i += 1
        return ''.join(res)