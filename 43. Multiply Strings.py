class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        s=[0]*(len(num1)+len(num2))
        for i,n1 in enumerate(num1[::-1]):
            for j,n2 in enumerate(num2[::-1]):
                s[i+j]+=int(n1)*int(n2)
                s[i+j+1]+=s[i+j]//10
                s[i+j]%=10
        while len(s)>1 and s[-1]==0:
            del s[-1]
        return ''.join(map(str,s[::-1]))