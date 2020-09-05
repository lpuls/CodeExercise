# _*_coding:utf-8_*_

class Solution:
    def impl(self, sequence):
        root = sequence[len(sequence) - 1]

        max_index = len(sequence) - 1

        index = 0
        while index < max_index:
            value = sequence[index]
            if value >= root:
                break
            index += 1
        
        temp = index
        while temp < max_index:
            value = sequence[temp]
            if value <= root:
                return False
            temp += 1
        
        result = True
        if index > 0:
            result = self.impl(sequence[:index])
        if max_index - index > 0:
            result &= self.impl(sequence[index:max_index])
        return result


    def VerifySquenceOfBST(self, sequence):
        if None is sequence or len(sequence) <= 0:
            return False
        return self.impl(sequence)

case = [
    [3, 2, 17, 14, 16, 10],
    [3, 2, 14, 17, 16, 10],
    [7,4,6,5],
    [13, 12, 11, 10],
    [7, 8, 9, 10]
]

s = Solution()

for item in case:
    print(item, s.VerifySquenceOfBST(item))