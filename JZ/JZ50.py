#  _*_coding:utf-8_*_

class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        if None is numbers:
            return False

        for item in numbers:
            if item >= len(numbers):
                return False

        index = 0
        while index < len(numbers):
            value = numbers[index]
            if numbers[value] == value and index != value:
                duplication[0] = value
                return True
            elif numbers[value] == value and index == value:
                index += 1
            else:
                numbers[value], numbers[index] = numbers[index], numbers[value]
        return False
        
s = Solution()
duplicate = [-1]
print(s.duplicate([2,3,1,0,2,5,3], duplicate), duplicate[0])

