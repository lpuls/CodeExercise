# _*_coding:utf-8_*_


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def PrintFromTopToBottom(self, root):
        s = list()
        if None is root:
            return s

        index = 0
        s.append(root)
        while index < len(s):
            node = s[index]
            s[index] = node.val
            index += 1

            if None is not node.left:
                s.append(node.left)
            if None is not node.right:
                s.append(node.right)
        return s

def spawn(data):
    if None is data or 0 >= len(data):
        return None

    root = TreeNode(data[0])
    queue = [root]
    
    index = 1
    while index < len(data):
        temp = queue[0]
        del queue[0]

        if None is not data[index]:
            temp.left = TreeNode(data[index])
            queue.append(temp.left)
        else:
            temp.left = None
        index += 1

        if index >= len(data):
            break
        
        if None is not data[index]:
            temp.right = TreeNode(data[index])
            queue.append(temp.right)
        else:
            temp.right = None
        index += 1
    
    return root
    

s = Solution()
case = [
    [1, 2, 3, 4, None, 5, None],
    [10,6,14,4,8,12,16]
]
for item in case:
    print(item)
    print(s.PrintFromTopToBottom(spawn(item)))
    print('\n')
