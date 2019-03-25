#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
# https://leetcode-cn.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (32.46%)
# Total Accepted:    62.4K
# Total Submissions: 192.3K
# Testcase Example:  '["flower","flow","flight"]'
#
# 编写一个函数来查找字符串数组中的最长公共前缀。
# 
# 如果不存在公共前缀，返回空字符串 ""。
# 
# 示例 1:
# 
# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 
# 
# 示例 2:
# 
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
# 
# 
# 说明:
# 
# 所有输入只包含小写字母 a-z 。
# 
#
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length = len(strs)
        if length <= 0:
            return ""

        prefix = strs[0]
        prefix_length = len(prefix)
        for i in range(0, length):
            current = strs[i]
            current_length = len(current)
            # 前缀比当前词汇大，找出当前词汇和前缀相同的部份
            if prefix_length > current_length:
                prefix = self.getPrefix(prefix, prefix_length, current, current_length)
                prefix_length = len(prefix)
            else:  # 找出当前词词是否存在该前缀
                if current[0: len(prefix)] != prefix:
                    prefix = self.getPrefix(current, current_length, prefix, prefix_length)
                    prefix_length = len(prefix)
        return prefix        

    def getPrefix(self, prefix, prefix_length, current, current_length):
        temp = ""
        for j in range(0, current_length):
            if prefix[j] != current[j]:
                break
            temp += current[j]
        return temp

# s = Solution()
# print(s.longestCommonPrefix(['abbcb', 'ab123', 'abgggg']))
# print(s.longestCommonPrefix(['a1bbcb', 'a2b123', 'a3bgggg']))
# print(s.longestCommonPrefix(['1a1bbcb', '2a2b123', '3a3bgggg']))

