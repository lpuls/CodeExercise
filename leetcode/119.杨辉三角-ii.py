#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#
class Solution:
    def getRow(self, rowIndex: int):  # -> List[int]:
        old_array = [1]
        new_array = list()
        for row in range(1, rowIndex + 1):
            index = row - 1

            last_num = 0
            for item in old_array:
                new_array.append(last_num + item)
                last_num = item

            new_array.append(last_num + 0)
            old_array, new_array = new_array, old_array
            new_array.clear()

        return old_array

# s = Solution()
# print(s.getRow(0))
# print(s.getRow(1))
# print(s.getRow(2))
# print(s.getRow(3))

