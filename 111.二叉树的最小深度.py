#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __get_depth__(self, root, depth):
        if not root:
            return depth - 1

        if not root.left:
            return self.__get_depth__(root.right, depth + 1)
        elif not root.right:
            return self.__get_depth__(root.left, depth + 1)
        else:
            return min(self.__get_depth__(root.left, depth + 1), 
                       self.__get_depth__(root.right, depth + 1))

    # 空的节点不算进最小的，当有一边节点为空时，只算另一边的高度
    def minDepth(self, root: TreeNode) -> int:
        return self.__get_depth__(root, 1)

# s = Solution()

# r = TreeNode(3)
# r.left = TreeNode(9)
# r.right = TreeNode(20)
# r.left.left = None
# r.left.right = None
# r.right.left = TreeNode(15)
# r.right.right = TreeNode(7)
# print(s.minDepth(r))

# r = TreeNode(1)
# r.left = None
# r.right = TreeNode(2)
# print(s.minDepth(r))

