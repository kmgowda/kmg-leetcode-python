// https://leetcode.com/problems/flower-planting-with-no-adjacent

class Solution(object):
    def gardenNoAdj(self, N, paths):
        """
        :type N: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        neighbors = dict() 
        for i, j in paths:
            neighbors.setdefault(i-1, []).append(j-1)
            neighbors.setdefault(j-1, []).append(i-1)
            
        flowers = [0]*N #flowers to be planted at garden 1, ... N
        for i in range(N): #garden 1-N
            available = {1, 2, 3, 4} #flower 1-4
            if i in neighbors: available -= {flowers[j] for j in neighbors[i]}
            flowers[i] = available.pop()
        return flowers        