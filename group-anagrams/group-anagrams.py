// https://leetcode.com/problems/group-anagrams

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ret = collections.defaultdict(list)
        for word in strs:
            key = ''.join(sorted(word))
            ret[key]+=[word]
        
        out = []
        for key in ret:
            out.append(ret[key])
        return out    
                