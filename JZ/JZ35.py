# _*_coding:utf-8_*_


class Solution:
    def InversePairs(self, data):
        if len(data) <= 0 and None is data:
            return 0
        
        count = self.meger(data, 0, len(data) - 1)
        return count % 1000000007

    def meger(self, data, start, end):
        if start >= end:
            return 0

        count = 0        
        mid = int((end - start) / 2) + start
        left = self.meger(data, start, mid)
        right = self.meger(data, mid + 1, end)

        temp = [None] * (end - start + 1)
        
        left_index = mid
        right_index = end
        tail_index = len(temp) - 1
        while left_index >= start and right_index > mid:
            if data[left_index] > data[right_index]:
                temp[tail_index] = data[left_index]
                count += (right_index - mid)
                if count >= 1000000007:
                    count = count % 1000000007
                left_index -= 1
            else:
                temp[tail_index] = data[right_index]
                right_index -= 1
            tail_index -= 1
        
        while left_index >= start:
            temp[tail_index] = data[left_index]
            left_index -= 1
            tail_index -= 1

        while right_index > mid:
            temp[tail_index] = data[right_index]
            right_index -= 1
            tail_index -= 1

        for index, value in enumerate(temp):
            data[start + index] = value
        
        return (count + left + right) % 1000000007


def force(array):
    count = 0
    for index, value in enumerate(array):
        for i in range(index + 1, len(array)):
            temp = array[i]
            if value > temp:
                count += 1
    return count


s = Solution()
print(s.InversePairs([2, 1, 3, 5, 7, 4, 6]))
print(s.InversePairs([2, 1, 3, 9, 5, 7]))
print(s.InversePairs([2, 1]))
print(s.InversePairs([1]))
print(s.InversePairs([364,637,341,406,747,995,234,971,571,219,993,407,416,366,315,301,601,650,418,355,460,505,360,965,516,648,727,667,465,849,455,181,486,149,588,233,144,174,557,67,746,550,474,162,268,142,463,221,882,576,604,739,288,569,256,936,275,401,497,82,935,983,583,523,697,478,147,795,380,973,958,115,773,870,259,655,446,863,735,784,3,671,433,630,425,930,64,266,235,187,284,665,874,80,45,848,38,811,267,575]))

print("")

print(force([2, 1, 3, 5, 7, 4, 6]))
print(force([2, 1, 3, 9, 5, 7]))
print(force([2, 1]))
print(force([1]))
print(force([364,637,341,406,747,995,234,971,571,219,993,407,416,366,315,301,601,650,418,355,460,505,360,965,516,648,727,667,465,849,455,181,486,149,588,233,144,174,557,67,746,550,474,162,268,142,463,221,882,576,604,739,288,569,256,936,275,401,497,82,935,983,583,523,697,478,147,795,380,973,958,115,773,870,259,655,446,863,735,784,3,671,433,630,425,930,64,266,235,187,284,665,874,80,45,848,38,811,267,575]))

        
