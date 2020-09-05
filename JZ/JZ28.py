# _*_coding:utf-8_*_

class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        total = dict()
        target = len(numbers) / 2

        for item in numbers:
            total[item] = total.get(item, 0) + 1

        for k, v in total.items():
            if v > target:
                return k
                
        return 0  

s = Solution()
case = [
    [1,2,3,2,4,2,5,2,3],
    [1,2,3,2,2,2,5,4,2],
    [1,2,3,4,5,6,7,8,8]
]

for item in case:
    print(s.MoreThanHalfNum_Solution(item))