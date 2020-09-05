#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#
# https://leetcode-cn.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (43.52%)
# Total Accepted:    44.5K
# Total Submissions: 102.1K
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 
# 示例:
# 
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
# 
# 
# 进阶:
# 
# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
# 
#
import sys

class Solution:
    # def maxSubArray(self, nums: List[int]) -> int:
    def maxSubArray(self, nums) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
        return max(dp)


# s = Solution()
# print(s.maxSubArray([1, 2]), 3)
# print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]), 6)
# print(s.maxSubArray([1]), 1)
# print(s.maxSubArray([8,-19,5,-4,20]), 21)
# print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]), 6)

