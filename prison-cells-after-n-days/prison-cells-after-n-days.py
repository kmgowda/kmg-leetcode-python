// https://leetcode.com/problems/prison-cells-after-n-days

class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        cells = [-1]+ cells+[-1]
        N -= max(N - 1, 0) / 14 * 14
        for _ in range(N):
            newcells = cells[:]
            for i in range(1, len(cells)-1):
                if (cells[i-1] == 0 and cells[i+1] == 0) or (cells[i-1] == 1 and cells[i+1] == 1):
                    newcells[i] = 1
                else:
                    newcells[i] = 0
            cells = newcells 
        return cells[1:-1]            