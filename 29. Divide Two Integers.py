class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        r=0
        flag=(dividend<0)^(divisor<0)
        dividend=abs(dividend)
        divisor=abs(divisor)
        while dividend>=divisor:
            s=divisor
            p=1
            while s<<1<=dividend:
                s<<=1
                p<<=1
            dividend-=s
            r+=p
        if flag:
            return max(-r,-2147483648)
        return min(r,2147483647)