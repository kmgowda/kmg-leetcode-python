// https://leetcode.com/problems/walls-and-gates

class Solution(object):
    
    def merge(self, i,j, R, C, rooms, val):
        if i < 0 or j < 0 or i >= R or j >= C or rooms[i][j] == -1 or rooms[i][j] < val:
            return
        rooms[i][j] = val
        val+=1
        self.merge(i+1, j, R, C, rooms, val)
        self.merge(i-1, j, R, C, rooms, val)
        self.merge(i, j+1, R, C, rooms, val)
        self.merge(i, j-1, R, C, rooms, val)
        
    
    
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        
        R = len(rooms)
        if not R :
            return
        C = len(rooms[0])
        for i in range(R):
            for j in range(C):
                if rooms[i][j] == 0:
                    self.merge(i,j, R, C, rooms, 0)
