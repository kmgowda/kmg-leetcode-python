// https://leetcode.com/problems/daily-temperatures

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        ans = [0]*len(temperatures)
        st = list()
              
        for i , t in enumerate(temperatures):
            while st and temperatures[st[-1]] < t:
                cur = st.pop()
                ans[cur]=i-cur
            st.append(i)
        return ans    