from collections import Counter
class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        l=len(words[0])
        m=len(words)
        d=Counter(words)
        i=0
        res=[]
        for k in range(l):
            left=k
            subd={}
            count=0
            for j in range(k, len(s)-l+1, l):
                tword=s[j:j+l]
                if tword in d:
                    if tword in subd:
                        subd[tword]+=1
                    else:
                        subd[tword]=1
                    count+=1
                    while subd[tword]>d[tword]:
                        subd[s[left:left+l]]-=1
                        left+=l
                        count-=1
                    if count==m:
                        res.append(left)
                else:
                    left=j+l
                    subd={}
                    count=0
        return res