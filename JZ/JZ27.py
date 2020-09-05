# _*_coding:utf-8_*_

class Solution:
    def Permutation(self, ss):
        if None is ss:
            return list()
        
        word = list()
        for item in ss:
            for index, w in enumerate(word):
                if item < w:
                    word.insert(index, item)
                    break
            else:
                word.append(item)

        exist = set()
        return self.impl(word, list(), exist)

    def impl(self, words, result, exist):
        if len(words) <= 0:
            for item in result:
                exist.add(item)
            return result
        
        self_result = list()
        for item in words:
            temp_result = list()
            if len(result) <= 0:
                temp_result.append(item)
            else:
                for r in result:
                    new_word = r + item
                    if new_word not in exist:
                        temp_result.append(r + item)
            temp = words[:]
            temp.remove(item)
            self_result += self.impl(temp, temp_result, exist)
        return self_result


            


s = Solution()
print(s.Permutation('ab'))