// https://leetcode.com/problems/exclusive-time-of-functions

class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        ans = [0]*n  
        stack = []
        m = len(logs)
        for i in range(m-1):
            line1 = logs[i].split(':')
            line2 = logs[i+1].split(':')
            if line1[1] == 'start':
                func = int(line1[0])
                time = int(line2[2]) - int(line1[2])
                stack.append([func, time])
            else:
                func, time = stack.pop(-1)
                ans[func] += time+1
                if stack:
                    stack[-1][1] += int(line2[2]) - int(line1[2]) - 1
                    
        ans[stack[0][0]] += stack[0][1]+1
        return ans