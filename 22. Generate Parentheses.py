class Solution:
    def generateParenthesis(self, n, open=0):
        if n == 0:
            return [')'*open]
        if open == 0:
            return ['('+x for x in self.generateParenthesis(n-1, 1)]
        else:
            return [')'+x for x in self.generateParenthesis(n, open-1)] + ['('+x for x in self.generateParenthesis(n-1, open+1)]
    '''def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if not n:
            return []
        left, right, ans = n, n, []
        self.dfs(left,right, ans, "")
        return ans

    def dfs(self, left, right, ans, string):
        if right<left:
            return
        if left==0 and right==0:
            ans.append(string)
            return
        if left:
            self.dfs(left-1, right, ans, string + "(")
        if right:
            self.dfs(left, right-1, ans, string + ")")'''