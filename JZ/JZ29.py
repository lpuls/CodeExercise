# _*_coding:utf-8_*_

class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if len(tinput) < k or k <= 0 or None is tinput:
            return []
        
        self.impl(tinput, 0, len(tinput) - 1)
        return tinput[: k]

    def impl(self, tinput, from_index, end_index):
        if from_index >= end_index:
            return

        stand = tinput[from_index]
        front = from_index
        tail = end_index

        while front < tail:
            while front < tail and tinput[tail] >= stand:
                tail -= 1
            if front < tail:
                tinput[front] = tinput[tail]
                front += 1

            while front < tail and tinput[front] < stand:
                front += 1
            if front < tail:
                tinput[tail] = tinput[front]
                tail -= 1
        
        tinput[front] = stand

        self.impl(tinput, from_index, front)
        self.impl(tinput, front + 1, end_index)            
        

s = Solution()

case = [
    ([4,5,1,6,2,7,3,8], 4),
    ([1,1,1,1,1,1,1,1], 4),
    ([], 4)
]

for item, k in case:
    print(s.GetLeastNumbers_Solution(item, k))


        
