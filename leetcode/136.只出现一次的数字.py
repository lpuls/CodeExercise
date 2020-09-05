#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#
class Solution:
    def singleNumber(self, nums: list) -> int:
        t = nums[0]
        for i in range(1, len(nums)):
            t = t ^ nums[i]
        return t

# s = Solution()
# print(s.singleNumber([2,2,1]))
# print(s.singleNumber([4,1,2,1,2]))

