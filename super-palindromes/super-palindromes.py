// https://leetcode.com/problems/super-palindromes

class Solution(object):
    def superpalindromesInRange(self, L, R):
        """
        :type L: str
        :type R: str
        :rtype: int
        """
        R = int(R)
        L = int(L)
        
        sqrt_sp = ['11', '22']
        
        for i in sqrt_sp:
            for j in ('0','1','2'):
                sqrt_sp.append(str(i[:1])+ j +str(i[1:]))
            if int(i) **2 > R:
                break
        sqrt_sp.append('1')
        sqrt_sp.append('2')
        sqrt_sp.append('3')
        
        ans  = 0
				
 
        for i in sqrt_sp:
            s = int(i)**2
            if L <= s <= R and str(s) == str(s)[::-1]:
                ans +=1
        return ans        