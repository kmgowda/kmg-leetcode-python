// https://leetcode.com/problems/can-place-flowers

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        tmp = [0]+flowerbed+[0]
        for i in range(1, len(tmp)-1):
            if tmp[i-1] == tmp[i] == tmp[i+1] == 0:
                tmp[i] = 1
                n-=1
        return n<1        
               