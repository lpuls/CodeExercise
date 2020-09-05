#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.__stack = list()
        self.__min = None

    def push(self, x: int) -> None:
        self.__stack.append(x)
        if None is self.__min or self.__min > x:
            self.__min = x

    def pop(self) -> None:
        if self.__stack.pop() == self.__min:
            if len(self.__stack) > 0:
                self.__min = self.__stack[0]
                for item in self.__stack:
                    if self.__min > item:
                        self.__min = item
            else:
                self.__min = None

    def top(self) -> int:
        if len(self.__stack) > 0:
            return self.__stack[-1]

    def getMin(self) -> int:
        return self.__min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(1)
# obj.push(-1)
# obj.push(0)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# print(obj.top())
# print(obj.getMin())


