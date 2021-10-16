// https://leetcode.com/problems/hamming-distance

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        s = x^y
        cnt=0
        while s > 0:
            s &= s-1
            cnt+=1
        return cnt    