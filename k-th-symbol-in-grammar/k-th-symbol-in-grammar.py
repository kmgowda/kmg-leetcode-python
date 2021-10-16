// https://leetcode.com/problems/k-th-symbol-in-grammar

class Solution(object):
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        return bin(K-1).count('1')%2  