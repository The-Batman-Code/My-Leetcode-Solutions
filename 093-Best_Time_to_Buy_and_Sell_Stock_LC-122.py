# Approach - 1
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] - prices[i] < 0:
                continue
            else:
                ans += prices[i + 1] - prices[i]
            print(ans)
        return ans


# Time : 67ms (12.46%) Space : 18.10 MB (6.72%)
