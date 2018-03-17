class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d={}
        for word in strs:
            key=''.join(sorted(word))
            d[key]=d.get(key,[])+[word]
        return list(d.values())