#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        """
        1. 进入空节点，说明父节点本身就不满足情况 0 == Sum - root.val，一定为False
        2. 没有左右节点时，说明为叶子节点，此时判断一下Sum - root.val是否为零
        3. 不满足以上条件时，进入左右节点再做判断
        """
        if not root:
            return False
        elif not root.left and not root.right:
            return (sum - root.val) == 0
        else:
            return self.hasPathSum(root.left, sum - root.val) \
                   or self.hasPathSum(root.right, sum - root.val)

# s = Solution()

# r = TreeNode(5)
# r.left = TreeNode(4)
# r.right = TreeNode(8)

# r.left.left = TreeNode(11)
# r.left.right = None

# r.left.left.left = TreeNode(7)
# r.left.left.right = TreeNode(2)

# r.right.left = TreeNode(13)
# r.right.right = TreeNode(4)

# r.right.right.right = TreeNode(1)

# print(s.hasPathSum(r, 22))

# print(s.hasPathSum(None, 0))

