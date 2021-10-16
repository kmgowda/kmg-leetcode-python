// https://leetcode.com/problems/happy-number

class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        st = set()
        while True:
            if n in st:
                return False
            st.add(n)            
            li = [int(i) for i in str(n)]
            n = 0
            for num in li:
                n+=num*num
            if n == 1:
                return True
