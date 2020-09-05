# _*_coding:utf-8_*_

class Solution:
    def GetUglyNumber_Solution(self, index):
        _2_index = 0
        _3_index = 0
        _5_index = 0

        ugly_index = 1
        ugly_array = [0] * index
        ugly_array[0] = 1

        for i in range(1, index):
            # 计算出下一个丑数；因为我们要有序，所以要取最小的值
            next_ugle = min(ugly_array[_2_index] * 2, ugly_array[_3_index] * 3, ugly_array[_5_index] * 5)
            
            # 将这个丑数记录下来，所于等下判断是哪个下标算出的值的及下一轮丑数记算的依据
            ugly_array[ugly_index] = next_ugle

            # 依次判断是2、3或5中的哪一个算出了本次丑数，并将其对应的下标往后移，用于计算下一个丑数
            if ugly_array[ugly_index] == ugly_array[_2_index] * 2:
                _2_index += 1
            if ugly_array[ugly_index] == ugly_array[_3_index] * 3:
                _3_index += 1
            if ugly_array[ugly_index] == ugly_array[_5_index] * 5:
                _5_index += 1

            # 丑数下标往后移
            ugly_index += 1
        return ugly_array[index - 1]
            



s = Solution()

print(s.GetUglyNumber_Solution(7))
print(s.GetUglyNumber_Solution(10))
print(s.GetUglyNumber_Solution(4))
print(s.GetUglyNumber_Solution(11))

print("")





