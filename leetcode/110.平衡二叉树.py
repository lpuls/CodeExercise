#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __get_depth__(self, root, depth):
        if not root:
            return True, depth - 1

        v, l = self.__get_depth__(root.left, depth + 1)
        if not v:
            return v, depth

        v, r = self.__get_depth__(root.right, depth + 1)
        if not v:
            return v, depth

        return abs(l - r) <= 1, max(l, r)

    def isBalanced(self, root: TreeNode) -> bool:
        v, _ = self.__get_depth__(root, 0)
        return v

# s = Solution()
# r = TreeNode(1)
# r.left = TreeNode(2)
# r.right = TreeNode(2)
# r.left.left = TreeNode(3)
# r.left.right = TreeNode(3)
# r.left.left.left = TreeNode(4)
# r.left.left.right = TreeNode(4)
# r.right.left = None
# r.right.right = None
# print(s.isBalanced(r))

