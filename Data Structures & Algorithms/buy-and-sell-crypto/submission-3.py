class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        final = 0
        left = 0
        right = 1
        while right < len(prices):
            if prices[left] < prices[right]:
                curr = prices[right] - prices[left]
                final = max(final, curr)
            else:
                left = right
            right += 1


        return final
                    

        