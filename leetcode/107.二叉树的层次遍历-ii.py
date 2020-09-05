#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层次遍历 II
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
    def levelOrderBottom(self, root):
        open = list()
        close = list()
        open.append((root, 0))
        while len(open) > 0:
            temp = open[0]
            temp_node = temp[0]
            temp_depth = temp[1]
            del open[0]
            
            if None is not temp_node:
                if temp_depth >= len(close):
                    close.insert(0, list())
                # python中，a[x] = a[-(len(a) + x)]
                close[-(temp_depth + 1)].append(temp_node.val)

                open.append((temp_node.left, temp_depth + 1))
                open.append((temp_node.right, temp_depth + 1))
            
        return close


# s = Solution()
# r = TreeNode(3)
# r.left = TreeNode(9)
# r.right = TreeNode(20)
# r.left.left = None
# r.left.right = None
# r.right.left = TreeNode(15)
# r.right.right = TreeNode(7)
# print(s.levelOrderBottom(r))

