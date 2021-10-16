// https://leetcode.com/problems/jewels-and-stones

class Solution:
    def numJewelsInStones1(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        map={}
        for i in J:
            map[i]=0
        for i in S:
            if i in map:
                map[i]+=1
        sum=0
        for i in map:
            sum+=map[i]
        return sum  

    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        sum=0
        for i in S:
            if i in J:
                sum+=1
        return sum        
    
    