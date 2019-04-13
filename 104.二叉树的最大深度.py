#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#
# https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/description/
#
# algorithms
# Easy (67.86%)
# Total Accepted:    40K
# Total Submissions: 58.6K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，找出其最大深度。
# 
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
# 
# 说明: 叶子节点是指没有子节点的节点。
# 
# 示例：
# 给定二叉树 [3,9,20,null,null,15,7]，
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 返回它的最大深度 3 。
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepthImpl(self, root, max_depth):
        if None is root:
            return max_depth
        else:
            return max(self.maxDepthImpl(root.left, max_depth + 1), self.maxDepthImpl(root.right, max_depth + 1))

    def maxDepth(self, root: TreeNode) -> int:
        return self.maxDepthImpl(root, 0)
        

# root = TreeNode(1) # 1

# root.left = TreeNode(2)   #2
# root.right = TreeNode(2)

# root.left.left = TreeNode(3)   #3
# root.left.right = TreeNode(4)
# root.right.left = TreeNode(4)
# root.right.right = TreeNode(3)

# root.right.right.right = TreeNode(3)  # 4

# root.right.right.right.right = TreeNode(3)  # 5

# s = Solution()
# print(s.maxDepth(root))

