// https://leetcode.com/problems/sort-characters-by-frequency

class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = collections.Counter(s)
        lt = list()
        for k in d:
            lt.append((d[k], k))
        lt=sorted(lt, reverse=True)
        ret=""
        for cnt,ch in lt:
            for i in range(cnt):
                ret+=ch
        return ret        
                
        
        