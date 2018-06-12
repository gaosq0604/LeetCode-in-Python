class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        from collections import deque
        queue = deque()
        for r in range(len(board)):
            for c in range(len(board[0])):
                if (r in [0, len(board)-1] or c in [0, len(board[0])-1]) and board[r][c] == 'O':
                    queue.append((r,c))
        while queue:
            r,c = queue.popleft()
            if 0<=r<len(board) and 0<=c<len(board[0]) and board[r][c] == 'O':
                board[r][c] = 'V'
                queue.append((r-1,c))
                queue.append((r+1,c))
                queue.append((r,c-1))
                queue.append((r,c+1))

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'V':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'