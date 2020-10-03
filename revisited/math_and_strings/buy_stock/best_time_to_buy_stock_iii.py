from typing import List


class Stock:

    def get_max_profit_(self, prices: List[int]) -> int:
        """
        Approach: Bi - directional DP
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param prices:
        :return:
        """
        days = len(prices)
        if days <= 1:
            return 0
        left_min, right_max = prices[0], prices[-1]
        left_profits = [0] * days
        right_profits = [0] * (days + 1)
        for left in range(1, days):
            left_profits[left] = max(left_profits[left - 1], prices[left] - left_min)
            left_min = min(left_min, prices[left])

            right = days - 1 - left
            right_profits[right] = max(right_profits[right + 1], right_max - prices[right])
            right_max = max(right_max, prices[right])
        max_profit = 0
        for i in range(0, days):
            max_profit = max(max_profit, left_profits[i] + right_profits[i + 1])
        return max_profit

    def get_max_profit(self, prices: List[int]) -> int:
        """
        Approach: One Pass Simulation
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param prices:
        :return:
        """
        transaction_1_cost = transaction_2_cost = float("inf")
        transaction_1_profit = transaction_2_profit = 0
        for price in prices:
            transaction_1_cost = min(transaction_1_cost, price)
            transaction_1_profit = max(transaction_1_profit, price - transaction_1_cost)

            transaction_2_cost = min(transaction_2_cost, price - transaction_1_profit)
            transaction_2_profit = max(transaction_2_profit, price - transaction_2_cost)
        return transaction_2_profit


if __name__ == "__main__":
    stock = Stock()
    print(stock.get_max_profit([3, 3, 5, 0, 0, 3, 1, 4]))
    print(stock.get_max_profit_([3, 3, 5, 0, 0, 3, 1, 4]))

