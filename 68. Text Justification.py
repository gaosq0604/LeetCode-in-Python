class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        length,cur,res=0,[],[]
        for w in words:
            if length+len(cur)+len(w)>maxWidth:
                for i in range(maxWidth-length):
                    cur[i%(len(cur)-1 or 1)]+=' '
                res.append(''.join(cur))
                length,cur=0,[]
            length+=len(w)
            cur.append(w)
        res.append(' '.join(cur).ljust(maxWidth))
        return res
            