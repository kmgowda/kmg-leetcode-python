// https://leetcode.com/problems/integer-to-english-words

class Solution(object):

    def create_below_twenty_str(self):
        num = list()
        num.append("")
        num.append("One")
        num.append("Two")
        num.append("Three")
        num.append("Four")
        num.append("Five")
        num.append("Six")
        num.append("Seven")
        num.append("Eight")
        num.append("Nine")
        num.append("Ten")
        num.append("Eleven")
        num.append("Twelve")
        num.append("Thirteen")
        num.append("Fourteen")
        num.append("Fifteen")
        num.append("Sixteen")
        num.append("Seventeen")
        num.append("Eighteen")
        num.append("Nineteen")
        return num
  
    def create_twodig_str(self):
        num = list()
        num.append("")
        num.append("")
        num.append("Twenty")
        num.append("Thirty")
        num.append("Forty")
        num.append("Fifty")
        num.append("Sixty")
        num.append("Seventy")
        num.append("Eighty")
        num.append("Ninety")
        return num 

  

    def convert_num_str(self, num, t1, t2):
        if num < 20:
            return t2[num]
        elif num < 100:
            if num%10:
                return t1[num//10]+" "+t2[num%10]
            else:
                return t1[num//10]
        elif num < 1000:
             ret = t2[num//100]+" Hundred"
             if num%100:
                return ret+" "+self.convert_num_str(num%100,t1, t2)
             else:
                return ret
        elif num < 1000000:
            ret = self.convert_num_str(num//1000, t1,t2)+" Thousand"
            if num%1000:
                return ret+" "+self.convert_num_str(num%1000,t1, t2)
            else:
                return ret
        elif num < 1000000000:
            ret = self.convert_num_str(num//1000000, t1,t2)+" Million"
            if num%1000000:
                return ret+" "+self.convert_num_str(num%1000000,t1, t2)
            else:
                return ret
        else:
            ret = self.convert_num_str(num//1000000000, t1,t2)+" Billion"
            if num%1000000000:
                return ret+" "+self.convert_num_str(num%1000000000,t1, t2)
            else:
                return ret           
 
    
    
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        t1 = self.create_twodig_str()
        t2 = self.create_below_twenty_str()
 
        
        if num == 0:
            return "Zero"
        else:
            return self.convert_num_str(num, t1,t2)