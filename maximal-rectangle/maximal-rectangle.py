// https://leetcode.com/problems/maximal-rectangle

class Solution(object):
    def maximalRectangle(self, matrix):
        
        def largestRectangleArea(height):
            height.append(0)
            stack, A = [0], 0
            for i in range(1, len(height)):
                while stack and height[stack[-1]] > height[i]: 
                    h = height[stack.pop()]
                    w = i if not stack else i-stack[-1]-1 
                    A = max(A, w*h)
                stack.append(i)
            return A
        
        
        if not matrix:
            return 0
        m, n, A = len(matrix), len(matrix[0]), 0
        height = [0 for _ in range(n)]
        for i in range(m):
            for j in xrange(n):
                height[j] = height[j]+1 if matrix[i][j]=="1" else 0
            A = max(A, largestRectangleArea(height))
        return A

            
 