# _*_coding:utf-8_*_

class Solution:
    def GetNumberOfK(self, data, k):
        if None is data or None is k or len(data) <= 0:
            return 0
        if data[len(data) - 1] < k or data[0] > k:
            return 0

        m = -1
        r = 0
        l = len(data) - 1
        while l - r > 1:
            m = int((r + l) / 2 + 0.5)
            if data[m] < k:
                r = m
            elif data[m] > k:
                l = m
            else:
                break
        
        
        count = 0
        r = m 
        while r >= 0 and data[r] == k:
            count += 1
            r -= 1

        l = m + 1
        while l < len(data) and data[l] == k:
            count += 1
            l += 1

        return count

        
s = Solution()

print(s.GetNumberOfK([1,3,3,3,3,4,5],2))
# print(s.GetNumberOfK(range(0, 100000), -1))
# print(s.GetNumberOfK([1, 2, 3, 4, 5, 6], 6))
# print(s.GetNumberOfK([1, 2, 3, 4, 5, 5, 5, 5, 6], 5))
# print(s.GetNumberOfK([], 5))
# print(s.GetNumberOfK(None, 5))
# print(s.GetNumberOfK([1, 2, 3, 4, 5], None))