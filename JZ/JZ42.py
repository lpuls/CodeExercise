#  _*_coding:utf-8_*_

class Solution:
    def FindNumbersWithSum(self, array, tsum):
        if None is array or len(array) <= 0 or array[0] >= tsum:
            return list()

        low = 0
        high = len(array) - 1

        result = list()

        while low < high:
            temp = array[low] + array[high]
            if temp == tsum:
                if 0 == len(result):
                    result = [array[low], array[high]]
                elif array[low] * array[high] < result[0] * result[1]:
                    result[0] = array[low] 
                    result[1] = array[high]
                low += 1
                high -= 1
            elif temp > tsum:
                high -= 1
            elif temp < tsum:
                low += 1

        return result
            

s = Solution()
print(s.FindNumbersWithSum([1, 2, 4, 7, 11, 16], 10))
print(s.FindNumbersWithSum([1, 2, 3, 4, 5, 6], 9))
print(s.FindNumbersWithSum([1, 2, 3, 4, 5], 1))
print(s.FindNumbersWithSum([], 1))
print(s.FindNumbersWithSum(None, 1))