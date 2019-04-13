#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#
# https://leetcode-cn.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (45.66%)
# Total Accepted:    28.3K
# Total Submissions: 61.6K
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# 给定一个二叉树，检查它是否是镜像对称的。
# 
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠/ \ / \
# 3  4 4  3
# 
# 
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠  \   \
# ⁠  3    3
# 
# 
# 说明:
# 
# 如果你可以运用递归和迭代两种方法解决这个问题，会很加分。
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    COMMIT1: 忘了root为空的情况了
    COMMIT2: 检查两边是否一边空一边非空时条件写错了
    """
    def isSymmetricImpl(self, left, right):
        if left and right:
            return left.val == right.val \
                and self.isSymmetricImpl(left.left, right.right) \
                and self.isSymmetricImpl(left.right, right.left)
        elif (not left and right) or (left and not right):
            return False
        else:
            return True

    def isSymmetric(self, root: TreeNode) -> bool:
        if None is root:
            return True
        return self.isSymmetricImpl(root.left, root.right)


# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(2)
# root.left.left = TreeNode(3)
# root.left.right = TreeNode(4)
# root.right.left = TreeNode(4)
# root.right.right = TreeNode(3)

# s = Solution()
# print(s.isSymmetric(root))

