// https://leetcode.com/problems/shortest-word-distance

class Solution(object):
    def shortestDistance1(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        d = collections.defaultdict(list)
        for i, word in enumerate(words):
            d[word]+=[i]
        dist = float('inf')
        for i in d[word1]:
            for j in d[word2]:
                dist=min(dist, abs(i-j))
        return dist 

    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        size = len(words)
        index1, index2 = size, size
        ans = size

        for i in range(size):
            if words[i] == word1:
                index1 = i
                ans = min(ans, abs(index1-index2))
            elif words[i] == word2:
                index2 = i
                ans = min(ans, abs(index1-index2))
        return ans    