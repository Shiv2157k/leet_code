from typing import List


class Stock:

    def get_max_profit_for_multiple_transactions_(self, prices: List[int]) -> int:
        """
        Approach: Peak Valley
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param prices:
        :return:
        """
        i = max_profit = 0

        while i < len(prices) - 1:
            while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
                i += 1
            valley = prices[i]
            while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
                i += 1
            peak = prices[i]
            max_profit += peak - valley
        return max_profit

    def get_max_profit_for_multiple_transaction(self, prices: List[int]) -> int:
        """
        Approach: One Pass
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param prices:
        :return:
        """
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        return max_profit

    def get_max_profit_for_one_transaction(self, prices: List[int]) -> int:
        """
        Approach: Greedy
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param prices:
        :return:
        """
        low_price, profit = float("inf"), 0
        for price in prices:
            low_price, profit = min(low_price, price), max(profit, price - low_price)
        return profit


if __name__ == "__main__":
    stock = Stock()
    print(stock.get_max_profit_for_one_transaction([7, 1, 5, 3, 6, 4]))
    print(stock.get_max_profit_for_multiple_transaction([7, 1, 5, 3, 6, 4]))
    print(stock.get_max_profit_for_multiple_transactions_([7, 1, 5, 3, 6, 4]))