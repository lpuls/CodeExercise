# _*_coding:utf-8_*_

from TreeHelper import *

class Solution:
    def IsBalanced_Solution(self, pRoot):
        if None is pRoot:
            return True
        return abs(self.impl(pRoot.right) - self.impl(pRoot.left)) <= 1
        

    def impl(self, pRoot):
        if None is pRoot:
            return 0

        return max(self.impl(pRoot.left), self.impl(pRoot.right)) + 1


s = Solution()

case = [
    [1, 2, 3, 4, 5, 6, 7],
    [1, None, 3, 6, 7],
    [1],
]

for item in case:
    print(s.IsBalanced_Solution(spawn(item)))