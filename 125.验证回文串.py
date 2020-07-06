#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#
class Solution:
    def isPalindrome(self, s: str) -> bool:
        ascii_a = ord('a')
        ascii_z = ord('z')
        ascii_cap_a = ord('a')
        ascii_cap_z = ord('z')
        ascii_0 = ord('0')
        ascii_9 = ord('9')

        count = 0
        stack = list()
        for item in s:
            ascii_item = ord(item)
            lower_item = item.lower()

            if ascii_a <= ascii_item <= ascii_z 
               or ascii_cap_a <= ascii_item <= ascii_cap_z
               or ascii_0 <= ascii_item <= ascii_9:
               
                if count <= 0:
                   stack.append(lower_item)
                elif stack[count - 1] == lower_item:
                    stack.pop()
                    count -= 1
                else:
                    stack.append(lower_item)
                    count += 1

s = Solution()
# print(False, s.isPalindrome('race a car'))
# print(True, s.isPalindrome('A man, a plan, a canal: Panama'))
# print(True, s.isPalindrome('a,IK,.?000111000?.,ki A'))
# print(True, s.isPalindrome('".,"'))
# print(True, s.isPalindrome('" "'))
# print(True, s.isPalindrome(''))

