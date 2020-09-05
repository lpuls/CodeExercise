# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if len(array) <= 0:
            return False
        
        row = 0
        col = len(array[0]) - 1
        
        while row < len(array) and col >= 0:
            if array[row][col] == target:
                return True
            elif array[row][col] < target:
                row += 1
            else:
                col -= 1
        return False

s = Solution()
cases = list()
cases.append((0, []))
cases.append((7, [[1, 2, 3, 4],[2, 3, 4, 5],[3, 4, 7, 9],[4, 7, 10, 13]]))
cases.append((14, [[1, 2, 3, 4],[2, 3, 4, 5],[3, 4, 7, 9],[4, 7, 10, 13]]))
cases.append((16,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]))

for item in cases:
   target = item[0]
   array = item[1]
   print(target)
   print(array)
   print(s.Find(target, array))