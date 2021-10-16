// https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation

class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        prime=[2,3,5,7,11,13,17,19,23]
        
        cnt=0
        for i in range(L,R+1):
            val = bin(i).count('1')
            if val in prime:
                cnt+=1
            #print("%s = %d , cnt=%d\n " %(bin(L), val,cnt))    
        return cnt        