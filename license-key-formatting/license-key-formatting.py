// https://leetcode.com/problems/license-key-formatting

class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        lt = S.split("-")
        tmp=""
        out=""
        ind= 0
        for i in range(ind, len(lt)):
            tmp+=lt[i]
         
        while tmp:
             p = tmp[-K:]
             out ="-"+p+out
             tmp=tmp[:-K]
        out=out[1:]        
        return out.upper()    
           
        
       
            