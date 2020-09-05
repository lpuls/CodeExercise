#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#
# https://leetcode-cn.com/problems/merge-sorted-array/description/
#
# algorithms
# Easy (43.29%)
# Total Accepted:    36.6K
# Total Submissions: 84.3K
# Testcase Example:  '[1,2,3,0,0,0]\n3\n[2,5,6]\n3'
#
# 给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。
# 
# 说明:
# 
# 
# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
# 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
# 
# 
# 示例:
# 
# 输入:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
# 
# 输出: [1,2,2,3,5,6]
# 
#
class Solution:
    def move_list(self, nums, start, value):
        for index in range(start, len(nums)):
            nums[index], value = value, nums[index]

    # def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    def merge(self, nums1, m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_index = 0
        nums2_index = 0

        while nums1_index < m and nums2_index < n:
            if nums1[nums1_index] > nums2[nums2_index]:
                self.move_list(nums1, nums1_index, nums2[nums2_index])
                m += 1
                nums2_index += 1
            nums1_index += 1

        while nums2_index < n:
            nums1[nums1_index] = nums2[nums2_index]
            nums1_index += 1
            nums2_index += 1

        # print(nums1)

# s = Solution()
# s.merge([1,2,3,0,0,0], 3, [2,5,6], 3)
# s.merge([4,5,6,0,0,0], 3, [1,2,3], 3)
# s.merge([0], 0, [1], 1)
# s.merge([4,0,0,0,0,0], 1, [1,2,3,5,6], 5)
# s.merge([-1,0,0,3,3,3,0,0,0], 6, [1,2,2], 3)

