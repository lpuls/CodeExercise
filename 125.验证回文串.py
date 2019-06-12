#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#
class Solution:
    def isPalindrome(self, s: str) -> bool:
        front = 0
        tail = len(s) - 1
        while front < tail:
            front_word = s[front]
            tail_word = s[tail]

            while front + 1 < len(s) and not front_word.isalnum():
                front += 1
                front_word = s[front]

            while tail - 1 >= 0 and not tail_word.isalnum():
                tail -= 1
                tail_word = s[tail]

            front += 1
            tail -= 1
            if front_word.lower() != tail_word.lower():
                return False
        return True

s = Solution()
# print(False, s.isPalindrome('race a car'))
# print(True, s.isPalindrome('A man, a plan, a canal: Panama'))
# print(True, s.isPalindrome('a,IK,.?000111000?.,ki A'))
# print(True, s.isPalindrome('".,"'))
# print(True, s.isPalindrome('" "'))
# print(True, s.isPalindrome(''))

