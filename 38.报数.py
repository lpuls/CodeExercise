#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 报数
#
# https://leetcode-cn.com/problems/count-and-say/description/
#
# algorithms
# Easy (48.60%)
# Total Accepted:    24.5K
# Total Submissions: 50.4K
# Testcase Example:  '1'
#
# 报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：
# 
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 
# 
# 1 被读作  "one 1"  ("一个一") , 即 11。
# 11 被读作 "two 1s" ("两个一"）, 即 21。
# 21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。
# 
# 给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。
# 
# 注意：整数顺序将表示为一个字符串。
# 
# 
# 
# 示例 1:
# 
# 输入: 1
# 输出: "1"
# 
# 
# 示例 2:
# 
# 输入: 4
# 输出: "1211"
# 
# 
#
class Solution:
    def countAndSay(self, n: int) -> str:
        result = '1'
        for i in range(2, n + 1):
            new_result = ''
            current_value = 0
            current_count = 0
            for item in result:
                value = int(item)
                if value != current_value:
                    if 0 != current_value:
                        new_result = new_result + str(current_count) + str(current_value)
                    current_count = 1
                    current_value = value
                else:
                    current_count += 1
            if 0 != current_value:
                new_result = new_result + str(current_count) + str(current_value)
            result = new_result
        return result

# s = Solution()
# print(s.countAndSay(4))

