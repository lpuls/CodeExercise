#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/description/
#
# algorithms
# Easy (44.50%)
# Total Accepted:    21.4K
# Total Submissions: 47.9K
# Testcase Example:  '[1,1,2]'
#
# 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
# 
# 示例 1:
# 
# 输入: 1->1->2
# 输出: 1->2
# 
# 
# 示例 2:
# 
# 输入: 1->1->2->3->3
# 输出: 1->2->3
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
    
#     def show(self):
#         t = self
#         while t:
#             print(t.val)
#             t = t.next

#     @staticmethod
#     def create(nums):
#         t = ListNode(0)
#         v = t
#         for item in nums:
#             v.next = ListNode(item)
#             v = v.next
#         return t.next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        node = head
        while node:
            if node.next and node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next
        return head

# s = Solution()
# s.deleteDuplicates(ListNode.create([1,1,2,2,4,4,4,4,5,6,7])).show()

