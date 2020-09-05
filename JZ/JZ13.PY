# _*_coding:utf-8_*_

class Solution:
    def reOrderArray(self, array):
        if None is array:
            return array

        count = 0
        for item in array:
            if item & 0x1:
                count += 1

        change = None
        current = 0
        even_index = count

        while current < len(array):
            value = array[current]
            print(array)
            if value & 0x1 and None is not change:
                if change != current:
                    array[current], array[change] = array[change], array[current]
                    array[current], array[even_index] = array[even_index], array[current]
                    even_index += 1
                else:
                    current += 1
                change += 1
            elif not value & 0x1 and None is change:
                change = current
                current += 1
            else:
                current += 1
        
        return array

s = Solution()
print(s.reOrderArray([1, 2, 3, 4, 5, 6, 7, 8]))