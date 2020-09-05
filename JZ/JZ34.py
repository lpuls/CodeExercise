# _*_coding:utf-8_*_

class Solution:
    def FirstNotRepeatingChar(self, s):
        if None is s or len(s) <= 0:
            return -1

        hash_table = dict()

        for index, item in enumerate(s):
            record = hash_table.get(item, 0)
            hash_table[item] = record + 1
        
        result = -1
        for index, item in enumerate(s):
            count = hash_table.get(item)
            if 1 == count:
                result = index
                break

        return result


s = Solution()

print(s.FirstNotRepeatingChar('abcabc'))
print(s.FirstNotRepeatingChar('abcdefg'))
print(s.FirstNotRepeatingChar(''))
print(s.FirstNotRepeatingChar(None))