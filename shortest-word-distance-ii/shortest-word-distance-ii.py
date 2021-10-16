// https://leetcode.com/problems/shortest-word-distance-ii

class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.d = collections.defaultdict(list)
        for i, word in enumerate(words):
            self.d[word]+=[i]

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        ret = float('inf')
        for i in self.d[word1]:
            for j in self.d[word2]:
                ret=min(ret, abs(i-j))
        return ret        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)