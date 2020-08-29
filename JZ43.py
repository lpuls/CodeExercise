#  _*_coding:utf-8_*_

class Solution:
    def LeftRotateString(self, s, n):
        if None is s or len(s) < n or n < 0:
            return s
        return s[n:] + s[:n]


s = Solution()
print(s.LeftRotateString('abcXYZdef', 3))