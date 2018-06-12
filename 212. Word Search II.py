class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.word = ''
        
class Solution:
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        self.m, self.n = len(board), len(board[0])
        self.res = []
        self.root = TrieNode()
        for word in set(words):
            node = self.root
            for ch in word:
                node = node.children[ch]
            node.word = word

        def dfs(i, j, node):
            node = node.children[board[i][j]]
            if node.word:
                self.res.append(node.word)
                node.word = ''
            tmp = board[i][j]
            board[i][j] = ''
            for a, b in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= a < self.m and 0 <= b < self.n and board[a][b] and board[a][b] in node.children:
                    dfs(a, b, node)
            board[i][j] = tmp
            
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] in self.root.children:
                    dfs(i, j, self.root)
        return self.res