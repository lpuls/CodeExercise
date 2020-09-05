# _*_coding:utf-8_*_

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        if None is pHead1 or None is pHead2:
            return None

        temp = dict()
        
        pTemp = pHead1
        while pTemp:
            temp[pTemp] = 1
            pTemp = pTemp.next

        pTemp = pHead2
        while pTemp:
            value = temp.get(pTemp, 0)
            if value + 1 >= 2:
                break
            pTemp = pTemp.next

        return pTemp


def spawn(list1, list2, common):
    p1 = None
    p2 = None
    head1 = p1
    head2 = p2

    if len(list1) > 0:
        p1 = ListNode(list1[0])
        head1 = p1
        for index in range(1, len(list1)):
            p1.next = ListNode(list1[index])
            p1 = p1.next

    if len(list2) > 0:
        p2 = ListNode(list2[0])
        head2 = p2
        for index in range(1, len(list2)):
            p2.next = ListNode(list2[index])
            p2 = p2.next

    for index in range(0, len(common)):
        new_node = ListNode(common[index])
        if None is p1:
            p1 = new_node
            head1 = p1
        else:
            p1.next = new_node

        if None is p2:
            p2 = new_node
            head2 = p2
        else:
            p2.next = new_node

        p1 = new_node
        p2 = new_node

    return head1, head2

def check(node):
    if None is node:
        print('None')
    else:
        print(node.val)


s = Solution()

check(s.FindFirstCommonNode(*spawn([], [], [1, 0, 0, 0])))
check(s.FindFirstCommonNode(*spawn([1, 2, 3, 4], [9, 8, 7, 6], [5])))
check(s.FindFirstCommonNode(*spawn([1, 2, 3, 4], [9, 8, 7, 6], [])))
check(s.FindFirstCommonNode(None, None))