# _*_coding:utf-8_*_

class Solution:
    def get_maybe(self, index, pushV):
        maybe = [None]
        
        j = index - 1
        while j >= 0:
            if None is not pushV[j]:
                maybe[0] = j
                break
            j -= 1
                
        j = index + 1
        while j < len(pushV):
            if None is not pushV[j]:
                maybe.append(j)
            j += 1
        
        return maybe

    def IsPopOrder(self, pushV, popV):
        if None is pushV or None is popV:
            return False
        if len(pushV) != len(popV) or len(pushV) <= 0 or len(popV) <= 0:
            return False
        
        val = popV[0]
        index = -1
        for i, value in enumerate(pushV):
            if val == value:
                index = i
                break
        
        if -1 == index:
            return False
            
        pushV[index] = None
        maybe = self.get_maybe(index, pushV)

        for i in range(1, len(popV)):
            val = popV[i]
            for maybeValue in maybe:
                if None is not maybeValue and maybeValue >= 0 and maybeValue < len(pushV) and val == pushV[maybeValue]:
                    index = maybeValue
                    pushV[index] = None
                    maybe = self.get_maybe(index, pushV)
                    break
            else:
                return False
        return True


s = Solution()

case_list = [
    ([1], [2]),
    ([1,2,3,4,5], [4,3,5,1,2]),
    ([1,2,3,4,5],[3,5,4,2,1]),
    ([1,2,3,4,5], [4,5,3,2,1]),
    ([1,2,3,4,], [4,5,3,2,1]),
    (None, [4,5,3,2,1])
]

for case in case_list:
    print(s.IsPopOrder(case[0], case[1]))