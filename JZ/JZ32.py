# _*_coding:utf-8_*_

class Solution:
    def PrintMinNumber(self, numbers):
        if len(numbers) <= 0 or None is numbers:
            return ""

        result_array = [list() for _ in range(len(numbers))]
        result_array[0].append(str(numbers[0]))

        result_min_value = numbers[0]
        for index in range(1, len(numbers)):
            last = result_array[index - 1]
            
            min_value = None
            min_seque = list()
            str_value = str(numbers[index])
            for i in range(0, len(last) + 1):
                temp = last[:]
                temp.insert(i, str_value)
                result = int(''.join(temp))
                if None is min_value or result <= min_value:
                    min_seque = temp
                    min_value = result
                    result_min_value = result
            result_array[index] = min_seque
        
        return result_min_value


s = Solution()

case = [
    [3,5,1,4,2],
    [3,32,321],
    [991, 9999, 1999],
    [321]
]

for item in case:
    print(s.PrintMinNumber(item))