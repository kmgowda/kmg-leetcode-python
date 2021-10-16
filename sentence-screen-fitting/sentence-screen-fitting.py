// https://leetcode.com/problems/sentence-screen-fitting

class Solution:
    def wordsTyping1(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        c = 0
        k = 0
        l = 0
        size = cols
        i = 0
        
        while i < rows:
            #print(sentence[k][l:])
            cl = len(sentence[k][l:])
            #print(i)
            if cl <= size:
                if cl < size:
                    size -= len(sentence[k][l:])+1
                else:
                    size = cols
                    i+=1
                k+=1
                l=0
                if k == len(sentence):
                     c+=1
                     k = 0
            else:
                if l > 0 and cl > cols:
                    l+= size
                size = cols
                i+=1
                
        return c        

    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """    
        s = ' '.join(sentence)+' '
        start, l = 0,len(s)
        for i in range(rows):
            start+=cols
            while s[start % l]!=' ':
                start-=1
            start+=1
        return start//l    
                
                
                
   