#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#
# https://leetcode-cn.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (37.04%)
# Total Accepted:    56.9K
# Total Submissions: 153.6K
# Testcase Example:  '"()"'
#
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
# 
# 有效字符串需满足：
# 
# 
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 
# 
# 注意空字符串可被认为是有效字符串。
# 
# 示例 1:
# 
# 输入: "()"
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: "()[]{}"
# 输出: true
# 
# 
# 示例 3:
# 
# 输入: "(]"
# 输出: false
# 
# 
# 示例 4:
# 
# 输入: "([)]"
# 输出: false
# 
# 
# 示例 5:
# 
# 输入: "{[]}"
# 输出: true
# 
#
class Solution:
    def isValid(self, s: str) -> bool:
        brackets_dict = {'[': ']', '(': ')', '{': '}' }

        length = len(s)
        stack = list()
        for item in s:
            if '[' == item or '(' == item or '{' == item:
                stack.append(item)
            else:
                stack_length = len(stack)
                if stack_length <= 0:
                    return False
                top = stack[len(stack) - 1]
                if brackets_dict[top] != item:
                    return False
                else:
                    stack.pop()
        return len(stack) == 0

# s = Solution()
# print(s.isValid('[][][][]([{[[[]]]}])'))
# print(s.isValid('[][][][]([{[[[[]]]}])'))

