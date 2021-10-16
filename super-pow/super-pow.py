// https://leetcode.com/problems/super-pow

class Solution(object):
    def superPow(self, a, b):
        if not b:
            return 1
        
        a = a % 1337
        ans = pow(a, b[len(b) - 1]) % 1337
        for i in range(len(b)-2, -1, -1):
            a = self.pow_mod(a, 10)
            ans = ans * pow(a, b[i]) % 1337
        return ans
    
    def pow_mod(self, a, b):
        ans = 1
        while b > 0:
            if b & 1 == 1:
                ans = ans * a % 1337
            a = a * a % 1337
            b = b >> 1
        return ans