# _*_coding:utf-8_*_

class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        if None is array or len(array) <= 0:
            return 0

        temp = 0
        for item in array:
            temp = temp ^ item

        diff_bit_index = 0
        for i in range(0, 32):
            bit_value = (temp >> i) & 1
            if bit_value:
                diff_bit_index = i
                break

        result = [0, 0]
        for item in array:
            bit_value = (item >> diff_bit_index) & 1
            if not bit_value:
                result[0] ^= item
            else:
                result[1] ^= item

        return result


s = Solution()
print(s.FindNumsAppearOnce([1,1,3,6]))
print(s.FindNumsAppearOnce([2, 4, 3, 6, 3, 2, 5, 5]))
# print(s.FindNumsAppearOnce([1, 2, 2, 3, 4, 5, 6, 7]))
# print(s.FindNumsAppearOnce([]))
# print(s.FindNumsAppearOnce([1]))
# print(s.FindNumsAppearOnce([1, 2, 3, 4, 5, 6]))