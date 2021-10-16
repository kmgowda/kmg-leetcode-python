// https://leetcode.com/problems/shortest-completing-word

class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
 
        d=collections.defaultdict(int)
        for c in licensePlate.lower():
            if c.isalpha():
                d[c]+=1
        mi = None       
        for word in words:
            tmp = d.copy()
            for c in word:
                if tmp[c] > 0:
                    tmp[c]-=1
    
            if not any(tmp.values()):
                if not mi or len(mi) > len(word):
                    mi=word
        return mi            
                