class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d=[]
        for ch in s:
            if ch=='(':
                d.append(')')
            elif ch=='{':
                d.append('}')
            elif ch=='[':
                d.append(']')
            elif ch==')' or '}' or ']':
                if len(d)==0 or d.pop()!=ch:
                    return False
            else:
                return False
        return d==[]