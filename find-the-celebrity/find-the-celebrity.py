// https://leetcode.com/problems/find-the-celebrity

# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n
        st = list()
        for i in range(n):
            st.append(i)

        while len(st) > 0:
            a = st.pop()
            if len(st) > 0:
                b = st.pop()
                if knows(a,b):
                    st.append(b)
                else:
                    st.append(a)
    
        for i in range(n):
            if i != a and (knows(a,i) or not knows(i,a)):
                return -1
        return a    
                
            