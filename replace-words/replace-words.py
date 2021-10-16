// https://leetcode.com/problems/replace-words

class Solution:
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        i = 1
        print(dict)
        while i < len(dict):
            if dict[i].startswith(dict[i-1]):
                dict.pop(i)
            else:
                i+=1
        lt = sentence.split()
        for i in range(len(lt)):
            for st in dict:
                if lt[i].startswith(st):
                    lt[i] = st
        st=lt[0]            
        for i in range(1, len(lt)):
            st+=" "+lt[i]
        return st    
            
                