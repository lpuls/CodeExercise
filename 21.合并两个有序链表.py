#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#
# https://leetcode-cn.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (53.39%)
# Total Accepted:    53.5K
# Total Submissions: 100.2K
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
# 
# 示例：
# 
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
# 
# 
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = None
        l1_node = l1
        l2_node = l2
        f = None
        while l1_node and l2_node:
            if l1_node.val < l2_node.val:
                if not result:
                    result = ListNode(l1_node.val)
                    f = result
                else:
                    result.next = ListNode(l1_node.val)
                    result = result.next
                l1_node = l1_node.next
            else:
                if not result:
                    result = ListNode(l2_node.val)
                    f = result
                else:
                    result.next = ListNode(l2_node.val)
                    result = result.next
                l2_node = l2_node.next
        while l1_node:
            t = ListNode(l1_node.val)
            result.next = t
            result = t
            l1_node = l1_node.next
        while l2_node:
            t = ListNode(l2_node.val)
            result.next = t
            result = t
            l2_node = l2_node.next
        return 

s = Solution()
l1 = ListNode(1)
t = l1
for v in range(10, 20, 3):
    t.next = ListNode(v)
    t = t.next 
l2 = ListNode(15)
t = l2
for v in range(0, 20, 4):
    t.next = ListNode(v)
    t = t.next
p = s.mergeTwoLists(l1, l2)
while p:
    print(p.val)
    p = p.next





