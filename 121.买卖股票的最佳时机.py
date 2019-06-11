#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#
class Solution:
    def maxProfit(self, prices: list) -> int:
        buy = None
        sell = 0
        for price in prices:
            if None is not buy:
                sell = max(sell, buy + price)
            
            if None is buy:
                buy = -price
            else:
                buy = max(buy, -price)
        return max(0, sell)

# s = Solution()
# print(s.maxProfit([2,1,2,1,0,1,2]))

