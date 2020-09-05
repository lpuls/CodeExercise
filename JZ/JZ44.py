#  _*_coding:utf-8_*_

class Solution:
    def ReverseSentence(self, s):
        if None is s or len(s) <= 0:
            return ""

        word = ""
        result = ""
        for item in s:
            if ' ' == item:
                result = word + result
                result = item + result
                word = ""
            else:
                word += item
        result = word + result 
        return result


s = Solution()
print(s.ReverseSentence("I am a student."))
print(s.ReverseSentence(""))
print(s.ReverseSentence(None))