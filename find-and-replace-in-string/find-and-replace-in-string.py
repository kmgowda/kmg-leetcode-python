// https://leetcode.com/problems/find-and-replace-in-string

class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        d ={}
        for i, ind in enumerate(indexes):
            d[ind]=[sources[i], targets[i]]
        start = 0
        out=""
        for ind in sorted(d.keys()):
            out+=S[start:ind]
            src, dst = d[ind]
            if src == S[ind:ind+len(src)]:
                out+=dst
            else:
                out+=S[ind:ind+len(src)]
            start = ind+len(src)
        out+=S[start:]    
                
        return out    