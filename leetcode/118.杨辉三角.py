#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#
class Solution:
    def generate(self, numRows: int):  # -> List[List[int]]:
        if numRows <= 0:
            return list()

        array = [[1]]
        for row in range(1, numRows):
            index = row - 1
            parent_array = array[index]

            last_num = 0
            new_array = list()
            for item in parent_array:
                new_array.append(last_num + item)
                last_num = item

            new_array.append(last_num + 0)
            array.append(new_array)
        return array

# s = Solution()
# print(s.generate(5))

