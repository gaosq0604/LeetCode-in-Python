class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ls=len(strs)
        if ls==0:
            return ''
        if ls==1:
            return strs[0]
        k=0
        min_len=999
        ptr=0
        for i in range(ls):
            if len(strs[i])<min_len:
                min_len=len(strs[i])
                ptr=i
        if min_len==0:
            return ''
        s=strs.pop(ptr)
        for i,ch in enumerate(s):
            for j in strs:
                if ch!=j[i]:
                    return s[:i]
        return s