// https://leetcode.com/problems/group-shifted-strings

class Solution:
    
    def get_key(self, word):
        ret="0"
        for i in range(1, len(word)):
            diff =  ord(word[i])-ord(word[i-1])
            if diff < 0:
                diff+=26
            ret+=str(diff)
        return ret    
       
    
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        map={}
        for word in strings:
            key= self.get_key(word)
            if key not in map:
                map[key]=list()
            map[key].append(word)
        ret = list()
        for key in map:
            ret.append(map[key])
        return ret    