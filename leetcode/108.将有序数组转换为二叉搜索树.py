#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#     def to_string(self, depth=1):
#         space = "#" * depth
#         r = str(self.val) + ":\n"
#         if self.left:
#             r = r + space + self.left.to_string(depth + 1)

#         if self.right:
#             r = r + space + self.right.to_string(depth + 1)
        
#         return r

import math


class Solution:
    def sortedArrayToBST(self, nums):
        if not nums and len(nums) <= 0:
            return None

        root = TreeNode(None)
        open = list()
        open.append((root, math.floor(len(nums) / 2), 0, len(nums)))
        while len(open) > 0:
            node = open[0][0]
            index = open[0][1]
            begin = open[0][2]
            end = open[0][3]
            value = nums[index]
            del open[0]

            node.val = value

            temp = math.floor((begin + index) / 2)
            if temp < index:
                node.left = TreeNode(None)
                open.append((node.left, temp, begin, index))

            temp = math.floor((end + index) / 2)
            if temp > index:
                node.right = TreeNode(None)
                open.append((node.right, temp, index + 1, end))
        return root

# s = Solution()
# print(s.sortedArrayToBST([-10, -3, 0, 5, 9]).to_string())
# print(s.sortedArrayToBST([-10, -3, 0, 5, 9]).to_string())
# print(s.sortedArrayToBST([]).to_string())


