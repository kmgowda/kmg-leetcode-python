// https://leetcode.com/problems/largest-rectangle-in-histogram

class Solution(object):
    # TLE
    def largestRectangleArea1(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        ma = 0
        N= len(heights)
        if N == 1: return heights[0]
        for i in range(N):
            p = -1
            for j in range(i-1, -1, -1):
                if heights[i] > heights[j]:
                    p = j
                    break
            l = heights[i]*(i-p)
            
            p = N
            for j in range(i+1, N):
                if heights[i] > heights[j]:
                    p = j
                    break
            r = heights[i]*(p-i-1)
            ma = max(ma, l+r)
            #print("%d: l=%d, r=%d, l+r=%d, max=%d" %(heights[i], l, r, l+r, ma))
        return ma 
    
    
    def largestRectangleArea(self, height):
        height.append(0)
        st = [-1]
        ans = 0
        for i in range(len(height)):
            while height[i] < height[st[-1]]:
                h = height[st.pop()]
                w = i - st[-1] - 1
                ans = max(ans, h * w)
            st.append(i)
        height.pop()
        return ans
    
                    