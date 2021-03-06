// https://leetcode.com/problems/read-n-characters-given-read4

# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        buf4 = [""] * 4  # read4 buffer 
        count = 0

        while n > 0:
            now = min(n, read4(buf4))
            if now == 0:  # no more to read
                break
            buf[count:count+now+1] = buf4  # copy from buf4 to buf
            count += now
            n -= now
        return count