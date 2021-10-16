// https://leetcode.com/problems/count-primes

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        
        ### Sieve of Eratosthenes ###
        # 1. Initialize a boolean array to store a flag for all numbers up to 'n'
        prime = [True]*(n)
        prime[0]= prime[1]=False
        i = 2 
        
        # 2. Starting from i=2 compute i**2, increment in muliples of 'i' and 
        # flag these as not prime.
        # The values are i**2, i(i+1), i(i+2), i(i+3)....
        while i*i <= n :
            if prime[i] == True:
                for j in range(i*i,n,i):
                    prime[j] = False 
            i += 1
        
        # When the algorithm terminates, all the numbers in the list that are marked as True 
        # are prime.
        """for p in range(2, n): 
            if prime[p]: 
                print p"""
            
        return prime.count(True) 