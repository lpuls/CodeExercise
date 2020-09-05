# _*_coding:utf-8_*_

from TreeHelper import *


class Solution:
    def TreeDepth(self, pRoot):
        if None is pRoot:
            return 0

        return max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right)) + 1

s = Solution()

case = [
    [1, None, 3, 6, 7],
    [1, 2, 3, 4, 5, 6, 7],
    [1],
]

for item in case:
    print(s.TreeDepth(spawn(item)))