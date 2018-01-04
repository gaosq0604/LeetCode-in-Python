class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0:
            return 0
        y=str(x)
        if y[0]=='-':
            s=y[0]
            y=y[1:]
        else:
            s=''
        while y[-1]=='0':
            y=y[:-1]
        y=y[::-1]
        y=int(s+y)
        if y>2147483647:
            return 0
        if y<-2147483648:
            return 0
        return y