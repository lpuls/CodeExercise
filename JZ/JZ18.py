# _*_coding:utf-8_*_

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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
    

def show(root):
    if None is root:
        print("None")
        return
    
    print(root.val)
    show(root.left)
    show(root.right)


class Solution:
    def Mirror(self, root):
        if None is root:
            return None

        temp = root.left
        root.left = root.right
        root.right = temp

        self.Mirror(root.left)        
        self.Mirror(root.right)   

        return root


case1 = [1, 2, 3, 4, None, 5, None]
case2 = []

s = Solution()

t1 = spawn(case1)
t2 = spawn(case1)
print("===> origin")
show(t1)
print("===> mirror")
s.Mirror(t2)
show(t2)

print("===>\n\n")

t1 = spawn(case2)
t2 = s.Mirror(spawn(case2))
print("===> origin")
show(t1)
print("===> mirror")
s.Mirror(t2)
show(t2)