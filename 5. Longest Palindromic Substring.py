class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        len_max=len(s)
        r_len=1
        result=s[0]
        if len_max<2:
            return s
        for i in range(len_max-1):
            k=r_len//2
            while (i-k>0) & (i+k<len_max-1):
                k+=1
                if s[i-k:i]==s[i+1:i+k+1][::-1]:
                    if 2*k+1>r_len:
                        r_len=2*k+1
                        result=s[i-k:i+k+1]
                else:
                    break
        if r_len==len_max:
            return result
        else:
            for i in range(len_max-1):
                if s[i]==s[i+1]:
                    if r_len<2:
                        r_len=2
                        result=s[i:i+2]
                    k=r_len//2-1
                    while (i-k>0) & (i+k<len_max-2):
                        k+=1
                        if s[i-k:i]==s[i+2:i+k+2][::-1]:
                            if 2*k+2>r_len:
                                r_len=2*k+2
                                result=s[i-k:i+k+2]
                        else:
                            break
        return result