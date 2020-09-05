#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#
# https://leetcode-cn.com/problems/length-of-last-word/description/
#
# algorithms
# Easy (29.09%)
# Total Accepted:    21.9K
# Total Submissions: 75K
# Testcase Example:  '"Hello World"'
#
# 给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。
# 
# 如果不存在最后一个单词，请返回 0 。
# 
# 说明：一个单词是指由字母组成，但不包含任何空格的字符串。
# 
# 示例:
# 
# 输入: "Hello World"
# 输出: 5
# 
# 
#
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        t = s.split(' ')
        while '' in t:
            t.remove('')
        length = len(t)
        if length <= 0:
            return 0
        return len(t[length - 1])

# s = Solution()
# print(s.lengthOfLastWord('Hello World'))
# print(s.lengthOfLastWord(" a "))
# print(s.lengthOfLastWord(""))

