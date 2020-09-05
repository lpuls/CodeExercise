#  _*_coding:utf-8_*_

class Solution:
    def IsContinuous(self, numbers):
        if None is numbers or len(numbers) < 5:
            return False

        min_index = 99
        temp = [0] * 14
        for item in numbers:
            if 0 != temp[item] and 0 != item:
                return False
            if 0 != item and item < min_index:
                min_index = item
            
            temp[item] += 1

        for index in range(min_index, min_index + len(numbers)):
            if 0 == temp[index] and 0 == temp[0]:
                return False
            elif 0 == temp[index] and 0 != temp[0]:
                temp[0] -= 1
        
        return True


s = Solution()
print(s.IsContinuous([1, 3, 2, 4, 6]))
print(s.IsContinuous([1, 3, 0, 0, 5]))
print(s.IsContinuous([1, 3, 2, 4, 5]))
