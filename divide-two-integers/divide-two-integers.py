// https://leetcode.com/problems/divide-two-integers

class Solution(object):
    def divide1(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = -1
        
        if ((dividend < 0)  and  (divisor < 0)):
            sign = 0
        if ((dividend > 0)  and  (divisor > 0)):    
            sign = 0
            


        dividend = abs(dividend); 
        divisor = abs(divisor); 
      
        if divisor == 1:
            quotient = dividend
        else:    
            quotient = 0; 
            while dividend >= divisor:
                 dividend-=divisor
                 quotient+=1
            
       
        if sign:
           quotient = -quotient
        
        return min(max(-2147483648,quotient),2147483647)
  
    """
    optimizations
        for example, if we want to calc (17/2)

        ret = 0;

        17-2 ,ret+=1; left=15

        15-4 ,ret+=2; left=11

        11-8 ,ret+=4; left=3

        3-2 ,ret+=1; left=1

        ret=8;


    """ 

    def divide(self, dividend, divisor):
        isMinus= ((dividend<0 and divisor >0) or (dividend>0 and divisor <0))
        dividend,divisor=abs(dividend),abs(divisor);
  
        shift = 0   
        while divisor << shift <= dividend:
            shift += 1
        ret = 0
        while dividend >= 0 and shift >= 0:
            if dividend >= divisor << shift:
                dividend -= divisor << shift
                ret += 1 << shift
            shift -= 1        

        if(isMinus):
            ret=-ret;
        return min(max(-2147483648,ret),2147483647);    
        
        
        
