class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not word:
            return True
        if not board:
            return False
        def dfs(board,i,j,word):
            if not word:
                return True
            if i<0 or j<0 or i>=m or j>=n or board[i][j]!=word[0]:
                return False
            board[i][j]='.'
            res=dfs(board,i+1,j,word[1:]) or dfs(board,i-1,j,word[1:]) or dfs(board,i,j+1,word[1:]) or dfs(board,i,j-1,word[1:])
            board[i][j]=word[0]
            return res
        m,n=len(board),len(board[0])
        for i in range(m):
            for j in range(n):
                if dfs(board,i,j,word):
                    return True
        return False
        