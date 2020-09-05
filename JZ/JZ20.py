# _*_coding:utf-8_*_

class Solution:
    def __init__(self):
        self._data = list()
        self._min = list()

    def push(self, node):
        self._data.append(node)
        for index in range(0, len(self._min)):
            val = self._min[index]
            if val >= node:
                self._min.insert(index, node)
                return
        self._min.append(node)

    def pop(self):
        if len(self._data) <= 0:
            return 0
        value = self._data[-1]
        del self._data[-1]

        
        for index in range(0, len(self._min)):
            val = self._min[index]
            if val == value:
                del self._min[index]
                break
        return value

    def top(self):
        if len(self._data) <= 0:
            return 0
        return self._data[-1]

    def min(self):
        if len(self._data) <= 0:
            return 0
        return self._min[0]


s = Solution()
case = [("PSH", 3),("MIN",),("PSH",4),("MIN",),("PSH",2),("MIN",),("PSH",3),("MIN",),("POP",),("MIN",),("POP",),("MIN",),("POP",),("MIN",),("PSH",0),("MIN",)]

r = list()
for item in case:
    cmd = item[0]
    if 'PSH' == cmd:
        s.push(item[1])
        print(cmd, item[1])
    elif 'MIN' == cmd:
        r.append(s.min())
        print(cmd, s.min())
    elif 'POP' == cmd:
        print(cmd, s.pop())
print(r)

