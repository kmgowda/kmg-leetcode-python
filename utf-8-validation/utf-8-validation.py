// https://leetcode.com/problems/utf-8-validation

class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        if not len(data):
            return False
        index = 0
        while index < len(data):
            bits=format(data[index], '08b')
            #print(bits)
            count = 0
            for b in bits:
                if b == '1':
                    count+=1
                else:
                    break
            index+=1        
            if not count:
                continue
            elif count == 1 or count > 4:
                return False
            else:
                count-=1
                while count > 0 and index < len(data):
                    bits=format(data[index], '08b')
                    #print(bits)
                    if bits[:2] != '10':
                        return False
                    index +=1
                    count -=1
                if count > 0:
                    return False
        return True        
                    
                
                
            