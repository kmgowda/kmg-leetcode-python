// https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n

class Solution(object):
    def queryString(self, S, N):
        """
        :type S: str
        :type N: int
        :rtype: bool
        """
        return all(bin(i)[2:] in S for i in xrange(N, N/2, -1))
        