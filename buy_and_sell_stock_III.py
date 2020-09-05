from typing import List


class Stock:

    def get_max_profit_(self, prices: List[int]):
        """
        Approach: DP bi-directional
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param prices:
        :return:
        """
        # base case
        if len(prices) <= 1:
            return 0

        left_min, right_max = prices[0], prices[-1]
        length = len(prices)
        left_profits, right_profits = [0] * length, [0] * (length + 1)

        # generating the left and right profits
        for left in range(1, length):
            left_profits[left] = max(left_profits[left - 1], prices[left] - left_min)
            left_min = min(left_min, prices[left])

            right = length - 1 - left

            right_profits[right] = max(right_profits[right + 1], right_max - prices[right])
            right_max = max(right_max, prices[right])

        max_profit = 0
        for i in range(length):
            max_profit = max(max_profit, left_profits[i] + right_profits[i + 1])
        return max_profit

    def get_max_profit(self, prices: List[int]):
        """
        Approach: Simulation
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param prices:
        :return:
        """
        t1_cost, t1_profit = float('inf'), 0
        t2_cost, t2_profit = float('inf'), 0

        for price in prices:
            t1_cost = min(t1_cost, price)
            t1_profit = max(t1_profit, price - t1_cost)

            t2_cost = min(t2_cost, price - t1_profit)
            t2_profit = max(t2_profit, price - t2_cost)
        return t2_profit


if __name__ == "__main__":

    stock = Stock()
    print(stock.get_max_profit_([3, 3, 5, 0, 0, 3, 1, 4]))
    print(stock.get_max_profit([3, 3, 5, 0, 0, 3, 1, 4]))