# _*_coding:utf-8_*_

class Solution:
    def Power(self, base, exponent):
        if 0 == base:
            return 0
        if 0 == exponent:
            return 1
        if 1 == exponent:
            return base;

        temp = abs(exponent)

        value = self.Power(base, temp >> 1)
        value = value * value

        if abs(exponent) & 0x1:
            value *= base

        if exponent < 0:
            return 1 / value
        return value


s = Solution()
for i in range(-10, 11):
    my = s.Power(2, i)
    std = pow(2, i)
    print(i, my, std, my == std)