#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#
class Solution:
    def convertToTitle(self, n: int) -> str:
        n -= 1
        r = ''
        t = ord('A')
        if n <= 26:
            return chr(t + n)
        else:
            i = int(n / 26)
            while i > 26:
                r += 'Z'
                i = int(i / 26)
            r = r + chr(t - 1 + i)

            j = i % 26
            return r + chr(t + j)

s = Solution()
# print(s.convertToTitle(1))
# print(s.convertToTitle(28))
print(s.convertToTitle(701))
print(s.convertToTitle(801))

