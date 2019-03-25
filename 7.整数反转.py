#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#
# https://leetcode-cn.com/problems/reverse-integer/description/
#
# algorithms
# Easy (32.12%)
# Total Accepted:    100.2K
# Total Submissions: 312K
# Testcase Example:  '123'
#
# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
# 
# 示例 1:
# 
# 输入: 123
# 输出: 321
# 
# 
# 示例 2:
# 
# 输入: -123
# 输出: -321
# 
# 
# 示例 3:
# 
# 输入: 120
# 输出: 21
# 
# 
# 注意:
# 
# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
# 
#
class Solution:
    def reverse(self, x: int) -> int:
        if not self.is_in_range(x):
            return 0

        is_less_zero = False
        if x < 0:
            is_less_zero = True
            x = abs(x)

        list_result = list(str(x))
        self.remove_zero(list_result)
        list_result.reverse()
        self.remove_zero(list_result)

        if len(list_result) <= 0:
            return 0

        result = int(list_result[0])
        for i in range(1, len(list_result)):
            result = result * 10 + int(list_result[i])
        if is_less_zero:
            result = -result

        if not self.is_in_range(result):
            return 0

        return result

    def remove_zero(self, input_list):
        del_list = []
        length = len(input_list)
        for i in range(0, length):
            if i < 0 or i >= len(input_list):
                break
            temp = input_list[i]
            if temp <= '0' or temp > '9':
                del_list.append(temp)
            else:
                break
        for item in del_list:
            input_list.remove(item)

    def is_in_range(self, x):
        return 2147483647 >= x and x >= -2147483648
        

