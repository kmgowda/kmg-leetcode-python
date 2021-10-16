// https://leetcode.com/problems/find-smallest-letter-greater-than-target

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        l =0
        h = len(letters)-1
        minc = letters[0]
        minv = None
        round = False
        fm = None
        while l <= h:
            m = (l+h)//2
            if fm == None:
                fm = m
            diff = ord(letters[m])-ord(target)
            if diff <= 0:
                diff +=26
                if round:
                    h = m-1
                else:    
                    l = m+1
            else:
                if round:
                    l = m+1
                else:    
                    h = m-1
            if not minv or diff < minv:
                minv = diff
                minc = letters[m]
            print("m = %d, l=%d, h=%d, diff=%d , letter=%c" %(m,l,h,diff, letters[m]))    
          
            if not round and l == len(letters):
               round = True 
               l = 0
               h = fm-1
 
        return minc       

    
    

