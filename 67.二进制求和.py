#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#
# https://leetcode-cn.com/problems/add-binary/description/
#
# algorithms
# Easy (47.16%)
# Total Accepted:    20.3K
# Total Submissions: 42.8K
# Testcase Example:  '"11"\n"1"'
#
# 给定两个二进制字符串，返回他们的和（用二进制表示）。
# 
# 输入为非空字符串且只包含数字 1 和 0。
# 
# 示例 1:
# 
# 输入: a = "11", b = "1"
# 输出: "100"
# 
# 示例 2:
# 
# 输入: a = "1010", b = "1011"
# 输出: "10101"
# 
#
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        r = ''
        s1 = a[::-1]        
        s2 = b[::-1]        
        add_value = 0
        for i in range(0, min(len(s1), len(s2))):
            v1 = int(s1[i])
            v2 = int(s2[i])
            t = v1 + v2 + add_value
            r = str(int(t % 2)) + r
            add_value = int(t / 2)
        if 0 != add_value:
            r = str(add_value) + r
        return r

s = Solution()
print(s.addBinary("1010", "1011"))
print(s.addBinary("11", "1"))

