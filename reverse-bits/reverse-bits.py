// https://leetcode.com/problems/reverse-bits

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ret = 0
        for i in range(32):
            ret = (ret<<1)| (n&1)
            n>>=1
        return ret    