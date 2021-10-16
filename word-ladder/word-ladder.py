// https://leetcode.com/problems/word-ladder

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        ret=[]
        layer={}
        layer[beginWord] = [[beginWord]]
        while layer:
            newlayer = collections.defaultdict(list)
            for w in layer:
                if w == endWord:
                    ret.extend(k for k in layer[w]) 
                else:
                    for i in range(len(w)):
                        for c in 'abcdefghijklmnopqrstuvwxyz':
                            neww=w[:i]+c+w[i+1:]
                            if neww in wordList:
                                newlayer[neww] += [[neww]+j for j in layer[w]]
            wordList-=set(newlayer.keys())
            layer=newlayer
        return min([len(k) for k in ret]) if ret else 0