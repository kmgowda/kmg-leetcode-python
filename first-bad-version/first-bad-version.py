// https://leetcode.com/problems/first-bad-version

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 0
        h = n
        b = 0
        while l <= h:
            m = (l+h)//2
            if isBadVersion(m):
                h = m-1
                b = m
            else:
                l = m+1
        return b        

                
        