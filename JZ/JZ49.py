#  _*_coding:utf-8_*_

class Solution:
    def StrToInt(self, s):
        if None is s or len(s) <= 0:
            return False

        min_value = ord('0')  
        max_value = ord('9')
        plus = ord('+')  
        sub = ord('-')  

        index = 1
        result = 0
        sign = 1
        for item in s[::-1]:
            temp = ord(item)
            if min_value <= temp <= max_value:
                result += index * (temp - min_value)
                index *= 10
            elif plus == temp:
                pass
            elif sub == temp:
                sign = -1
            else:
                return False

        return result  * sign


s = Solution()
print(s.StrToInt('1234'))
print(s.StrToInt('+1234'))
print(s.StrToInt('-1234'))
print(s.StrToInt('a1234'))
print(s.StrToInt('1234b'))
print(s.StrToInt('abcdb'))