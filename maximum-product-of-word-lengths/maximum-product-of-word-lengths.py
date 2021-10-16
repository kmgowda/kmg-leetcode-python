// https://leetcode.com/problems/maximum-product-of-word-lengths

class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        d = {}
        for w in words:
            d[w] = set(w)
        
        ans = 0
        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                if not (d[words[i]] & d[words[j]]):
                    ans = max(ans, len(words[i]) * len(words[j]))
        return ans    