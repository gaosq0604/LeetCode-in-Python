class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        d={'2': ['a', 'b', 'c'],
         '3': ['d', 'e', 'f'],
         '4': ['g', 'h', 'i'],
         '5': ['j', 'k', 'l'],
         '6': ['m', 'n', 'o'],
         '7': ['p', 'q', 'r', 's'],
         '8': ['t', 'u', 'v'],
         '9': ['w', 'x', 'y', 'z']}
        r=[]
        if digits=='':
            return []
        if len(digits)==1:
            return list(d[digits])
        a=[d[i] for i in digits]
        from functools import reduce
        return reduce((lambda x, y: [i + j for i in x for j in y]), a) 