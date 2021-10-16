// https://leetcode.com/problems/valid-sudoku

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        d=collections.defaultdict(bool)
        for i in range(9):
            for j in range(9):
                if board[i][j] !='.':
                    st="("+board[i][j]+")"
                    if d[st+str(i)] or d[str(j)+st] or d[str(i//3)+st+str(j/3)]:
                        return False
                    d[st+str(i)] = True
                    d[str(j)+st] = True
                    d[str(i//3)+st+str(j/3)] = True
        return True            
                    
