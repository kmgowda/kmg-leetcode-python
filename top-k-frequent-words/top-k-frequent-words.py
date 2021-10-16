// https://leetcode.com/problems/top-k-frequent-words

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        lt=collections.Counter(words).items()
        lt.sort(key=lambda(i,v):(-v,i))
        return [i for i,v in lt[:k]]