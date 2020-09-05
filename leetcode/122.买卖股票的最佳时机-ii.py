#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#
class Solution:
    """
    只要关心赚钱就行，因此用贪心把所有能赚钱的机会加到一起就行
    """
    def maxProfit(self, prices: list) -> int:
        sum = 0
        for index in range(1, len(prices)):
            sum += max(0, prices[index] - prices[index - 1])
        return sum

# s = Solution()
# print(s.maxProfit([7,1,5,3,6,4]))
# print(s.maxProfit([1,2,3,4,5]))
# print(s.maxProfit([7,6,4,3,1]))
