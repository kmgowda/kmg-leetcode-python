// https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times

# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def __init__(self):
        self.queue = []
    def read(self, buf, n):
        read, need, buff = 0, n, ['']*4
        while need > 0:
            k = read4(buff)
            self.queue.extend(buff[:k])
            need = min(len(self.queue), n - read)
            buf[read:read+need] = [self.queue.pop(0) for _ in range(need)]
            read += need
        return read