from typing import List


class Stock:

    def max_profit(self, prices: List[int]) -> int:
        """
        Approach: One Pass
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param prices:
        :return:
        """
        profit = 0
        for idx in range(1, len(prices)):
            if prices[idx] > prices[idx - 1]:
                profit += prices[idx] - prices[idx - 1]
        return profit

    def max_profit_(self, prices: List[int]) -> int:
        """
        Approach: Peak Valley
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param prices:
        :return:
        """
        idx = max_profit = 0
        while idx < len(prices) - 1:
            while idx < len(prices) - 1 and prices[idx] >= prices[idx + 1]:
                idx += 1
            valley = prices[idx]
            while idx < len(prices) - 1 and prices[idx] <= prices[idx + 1]:
                idx += 1
            peak = prices[idx]
            max_profit += peak - valley
        return max_profit


if __name__ == "__main__":
    stock = Stock()
    print(stock.max_profit([7, 1, 5, 3, 6, 4]))
    print(stock.max_profit_([7, 1, 5, 3, 6, 4]))