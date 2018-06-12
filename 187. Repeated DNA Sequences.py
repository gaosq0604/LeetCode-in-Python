class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        from collections import Counter
        counter = Counter()
        counter.update(s[i:i+10] for i in range(len(s)-9))
        return [key for key, val in counter.items() if val > 1]