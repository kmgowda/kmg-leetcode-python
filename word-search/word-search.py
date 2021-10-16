// https://leetcode.com/problems/word-search

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def search(board, word, i, j, M, N,d):
            if not word:
                return True
            if (0 <= i < M) and  (0 <= j < N) and not d[i][j]:
                if word[0] == board[i][j]:
                    d[i][j] = True
                    word = word[1:]
                    ret = (search(board, word, i+1, j, M, N, d) or search(board, word, i-1, j, M, N, d) or
                        search(board, word, i, j+1, M, N, d) or search(board, word, i, j-1, M, N, d))
                    d[i][j] = False
                    return ret
                    
            return False
        
        M = len(board)
        N = len(board[0])
        for i in range(M):
            for j in range(N):
                if board[i][j] == word[0]:
                    d = [[False]*N for _ in range(M)]
                    if search(board, word, i, j, M, N, d):
                        return True
        return False        
        