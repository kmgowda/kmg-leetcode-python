// https://leetcode.com/problems/spiral-matrix

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ret = list()
        M = len(matrix)
        if not M:
            return ret
        N = len(matrix[0])
        
        rh = M-1
        ch = N-1
        rl = 0
        cl = 0
        while rl < rh and cl < ch:
            
            for i in range(cl, ch):
                ret.append(matrix[rl][i])
            
            for i in range(rl, rh):
                ret.append(matrix[i][ch])
            
            for i in range(ch, cl, -1):
                ret.append(matrix[rh][i])
            
            for i in range(rh, rl, -1):
                ret.append(matrix[i][cl])
                
            rl+=1
            rh-=1
            cl+=1
            ch-=1
#        print(ret)          
        if M == N and N&1 == 1:
            ret.append(matrix[rh][ch])
        else:
            if rl == rh and cl < (ch+1):
                for i in range(cl, ch+1):
                    ret.append(matrix[rl][i])
            elif cl == ch and rl < (rh+1): 
                for i in range(rl, rh+1):
                    ret.append(matrix[i][cl])
#            print(ret)
            
        return ret    
        