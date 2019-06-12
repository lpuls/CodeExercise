#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#
class Solution:
    def twoSum(self, numbers: list, target: int) -> list:
        l = 0
        r = len(numbers) - 1
        while l < r:
            v = numbers[l] + numbers[r]
            if v == target:
                return [l + 1, r + 1]
            elif v > target:
                r -= 1
            else:
                l += 1

# s = Solution()
# print(s.twoSum([2, 7, 11, 15], 9))

