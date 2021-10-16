// https://leetcode.com/problems/letter-combinations-of-a-phone-number

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        d={'1':[], '2':['a', 'b', 'c'], '3':['d', 'e', 'f'], '4':['g', 'h', 'i'], '5':['j', 'k', 'l'], 
           '6':['m','n','o'], '7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z']}
        
        
        def build(st):
            if not st:
                return ['']
            
            ret=[]
            lt = build(st[1:])
            for c in d[st[0]]:
                for s in lt:
                    ret.append(c+s)
            return ret
        
        if not digits:
            return []
        
        return build(digits)
        