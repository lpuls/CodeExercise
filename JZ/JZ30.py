# _*_coding:utf-8_*_

class Solution:
    def FindGreatestSumOfSubArray(self, array):
        if None is array or len(array) <= 0:
            return 0

        result_array = list()
        for item in array:
            result_array.append(list())

        result_array[0].append(array[0])
        max_value = array[0]

        for index in range(1, len(array)):
            item = array[index]
            for value in result_array[index - 1]:
                result_array[index].append(item + value)
                if item + value > max_value:
                    max_value = item + value
            result_array[index].append(item)
            if item > max_value:
                max_value = item
        
        return max_value

s = Solution()

case = [
    [6,-3,-2,7,-15,1,2,2]
]

s.FindGreatestSumOfSubArray(case)
            
        