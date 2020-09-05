#  _*_coding:utf-8_*_


class Solution:
    def FindContinuousSequence(self, tsum):
        if tsum <= 0:
            return list()

        target = int((tsum + 1) / 2)
        current_sum = 1
        begin = 1
        front = 2

        result = list()
        while begin < target:
            if current_sum > tsum:
                current_sum -= begin
                begin += 1
            elif current_sum <= tsum:
                current_sum += front
                front += 1

            if current_sum == tsum:
                result.append(list(range(begin, front)))

        return result


s = Solution()
print(s.FindContinuousSequence(9))
print(s.FindContinuousSequence(3))
print(s.FindContinuousSequence(10))
print(s.FindContinuousSequence(100))
