class Solution:
    def is_valid(self,array):
        array=[i for i in array if i != '.']
        return len(set(array)) == len(array)
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        s=[]
        for i,row in enumerate(board):
            for j,c in enumerate(row):
                if c!='.':
                    s+=(i,c),(c,j),(i//3,j//3,c)
        return len(s)==len(set(s))
        '''for row in board:
            if not self.is_valid(row):
                return False
        for col in zip(*board):
            if not self.is_valid(col):
                return False
        for i in (0,3,6):
            for j in (0,3,6):
                s=[board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not self.is_valid(s):
                    return False
        return True'''