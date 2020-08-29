#  _*_coding:utf-8_*_

class Solution:
    def multiply(self, A):
        if None is A or len(A) <= 0:
            return list()

        temp1 = [1] * len(A)
        temp2 = [1] * len(A)

        for index in range(1, len(A)):
            temp1[index] = temp1[index - 1] * A[index - 1]
            temp2[-(index + 1)] = temp2[-index] * A[-index]

        result = list()
        for index, value in enumerate(temp1):
            v2 = temp2[index]
            result.append(value * v2)

        return result


s = Solution()
print(s.multiply([1, 2, 3, 4, 5]))
