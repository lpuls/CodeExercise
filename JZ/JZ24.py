# _*_coding:utf-8_*_

from TreeHelper import *

class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        if None is root:
            return []

        temp = expectNumber - root.val
        if temp < 0:
            return []
        elif temp == 0:
            if None is root.left and None is root.right:
                return [[root.val]]
            else:
                return []
        else:
            if None is root.left and None is root.right:
                return []
            else:
                left_path = self.FindPath(root.left, temp)
                right_path = self.FindPath(root.right, temp)
                
                path = left_path + right_path
                for item in path:
                    item.insert(0, root.val)
                return path



s = Solution()

case = [
    [(10,5,12,4,7), 22],
    [(10, 2, 16, 1, 3, 14, 17), 15],
    [(10, 2, 4, 3, 3, 1, 1), 15],
    # [(10, None, 11, None, None, None, 12, None, None, None, None, None, None, None, 13), 46],
]

for tree, value in case:
    path = s.FindPath(spawn(tree), value)
    if None is path:
        print(None)
        continue

    print(path)
    