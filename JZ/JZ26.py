# _*_coding:utf-8_*_

from TreeHelper import *

class Solution:
    def impl(self, pRootOfTree):
        if None is pRootOfTree:
            return None

        pre_node = self.impl(pRootOfTree.left)
        next_node = self.impl(pRootOfTree.right)

        return_node = pRootOfTree
        if None is not pre_node:
            pre_node.right = pRootOfTree
            pRootOfTree.left = pre_node
        
        if None is not next_node:
            min_node = next_node
            while None is not min_node.left:
                min_node = min_node.left

            pRootOfTree.right = min_node
            min_node.left = pRootOfTree

            return_node = next_node
        
        return return_node

        

    def Convert(self, pRootOfTree):
        node = self.impl(pRootOfTree)

        while node:
            if None is node.left:
                break
            node = node.left
        return node


s = Solution()

case = [
    [10, 5, 15, 2, 7, 12, 17, 1, 3, 6, 8, 11, 14, 16, 19],
    [10,5,12,4,7],
    [10, 2, 16, 1, 3, 14, 17],
    [10, 2, 4, 3, 3, 1, 1],
]

for tree in case:
    list_node = s.Convert(spawn(tree))
    while None is not list_node:
        print(list_node.val, end='\t')
        list_node = list_node.right
    print('')
