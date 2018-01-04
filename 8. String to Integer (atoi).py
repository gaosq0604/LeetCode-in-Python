class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        INT_MAX=2147483647
        INT_MIN=-2147483648
        str=str.strip()
        if len(str)==0:
            return 0
        flag=1
        if str[0]=='+':
            str=str[1:]
        elif str[0]=='-':
            flag=-1
            str=str[1:]
        if len(str)==0:
            return 0
        k=0
        while str[k]>='0' and str[k]<='9':
            k+=1
            if k==len(str):
                break
        if k==0:
            return 0
        result=str[0:k]
        r=int(result)*flag
        if r>INT_MAX:
            return INT_MAX
        elif r<INT_MIN:
            return INT_MIN
        else:
            return r