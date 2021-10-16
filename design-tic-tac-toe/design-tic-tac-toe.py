// https://leetcode.com/problems/design-tic-tac-toe

class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.mat = [[0]*n for _ in range(n)]
        self.size = n
        

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        self.mat[row][col] = player
        flag = True
        for i in range(self.size):
            if self.mat[row][i] != player:
                flag = False
                break
        if flag:
            return player
        flag = True
        for i in range(self.size):
            if self.mat[i][col] != player:
                flag= False
                break
        if flag:
            return player
        
        if abs(row-col) != abs(col-row):
            return  0
        
 
        flag = True
        for i in range(self.size):
            if self.mat[i][i] != player:
                flag = False
                break
        if flag:
            return player

        flag = True
        for i in range(self.size):
            if self.mat[i][self.size-i-1] != player:
                flag = False
                break
        
        if flag:
            return player
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)