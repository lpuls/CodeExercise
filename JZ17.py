#  _*_coding:utf-8_*_
'''
树的子结构
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def eq(a, b):
    return abs(a - b) < 0.00001


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        if None is pRoot1:
            return False
        if None is pRoot2:
            return False

        return self.has_sub_tree_impl(pRoot1, pRoot2, pRoot2)

    def has_sub_tree_impl(self, pRoot1, pRoot2, pOrigin):
        if None is pRoot1 and None is not pRoot2:
            return False
        if None is not pRoot1 and None is pRoot2:
            return False
        if None is pRoot1 and None is pRoot2:
            return True

        if eq(pRoot1.val, pRoot2.val):
            return self.has_sub_tree_impl(pRoot1.left, pRoot2.left, pOrigin) \
                and self.has_sub_tree_impl(pRoot1.right, pRoot2.right, pOrigin)
        else:
            return self.has_sub_tree_impl(pRoot1.left, pRoot2, pOrigin) \
                or self.has_sub_tree_impl(pRoot1.right, pRoot2, pOrigin)


def spawn(data):
    if None is data or len(data) <= 0:
        return None
    
    # (value, left, right)
    root = TreeNode(data[0])
    root.left = spawn(data[1])
    root.right = spawn(data[2])
    return root


t1 = spawn((1, (2, (4, None, None), (5, None, None)), (3, (6, None, None), (7, None, None))))
t5 = spawn((1, (2, (2, (4, None, None), (5, None, None)), (5, None, None)), (3, (6, None, None), (7, None, None))))
t2 = spawn((2, (4, None, None), (5, None, None)))
t3 = spawn((2, None, (5, None, None)))
t4 = spawn((2, None, None))

# {8,8,7,9,2,#,#,#,#,4,7},{8,9,2}
jt1 = spawn((8, (8, (9, None, None), (2, None, None)), (7, (4, None, None), (7, None, None))))
jt2 = spawn((8, (9, None, None), (2, None, None)))

s = Solution()
print(s.HasSubtree(t1, t2))
print(s.HasSubtree(t1, t3))
print(s.HasSubtree(t1, t4))
print(s.HasSubtree(t5, t2))
print(s.HasSubtree(t5, t3))
print(s.HasSubtree(t5, t4))
print(s.HasSubtree(t1, None))
print(s.HasSubtree(None, t2))
print("==============")
print(s.HasSubtree(jt1, jt2))
