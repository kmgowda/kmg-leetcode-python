// https://leetcode.com/problems/push-dominoes

class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        while(True):
            new = dominoes.replace('R.L', 'S')
            new = new.replace('.L','LL').replace('R.','RR')
            if new == dominoes:
                break
            else:
                dominoes = new
        return dominoes.replace('S', 'R.L')