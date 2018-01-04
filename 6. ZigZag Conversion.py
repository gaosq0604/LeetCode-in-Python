class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        #length=len(s)
        #result=''
        if numRows==1:
            return s
        '''if numRows==2:
            result+=s[::2]
            result+=s[1::2]
            return result
        loop=2*numRows-2
        result+=s[::loop]
        for i in range(1,numRows-1):
            s1=s[i::loop]
            s2=s[loop-i::loop]
            for j in range(len(s2)):
                result+=s1[j]
                result+=s2[j]
            if len(s1)>len(s2):
                result+=s1[-1]
        result+=s[numRows-1::loop]
        return result'''
        result=['']*numRows
        index,step=0,1
        for x in s:
            result[index]+=x
            if index==0:
                step=1
            elif index==numRows-1:
                step=-1
            index+=step
        return ''.join(result)
        
        