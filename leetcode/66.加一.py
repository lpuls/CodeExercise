#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#
# https://leetcode-cn.com/problems/plus-one/description/
#
# algorithms
# Easy (37.92%)
# Total Accepted:    44.1K
# Total Submissions: 115.9K
# Testcase Example:  '[1,2,3]'
#
# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
# 
# 最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。
# 
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
# 
# 示例 1:
# 
# 输入: [1,2,3]
# 输出: [1,2,4]
# 解释: 输入数组表示数字 123。
# 
# 
# 示例 2:
# 
# 输入: [4,3,2,1]
# 输出: [4,3,2,2]
# 解释: 输入数组表示数字 4321。
# 
# 
#
class Solution:
    def plusOne(self, digits):
        add_value = 1
        for i in range(len(digits) - 1, -1, -1):
            value = digits[i] + add_value
            digits[i] = int(value % 10)
            add_value = int(value / 10)
        if 0 != add_value:
            digits.insert(0, add_value)
        return digits

# s = Solution()
# print(s.plusOne([4,3,2,1]))
# print(s.plusOne([9,9,9,9]))

