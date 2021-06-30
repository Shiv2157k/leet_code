from typing import List


class Stock:

    def max_profit(self, prices: List[int]) -> int:
        """
        Approach: Greedy (One Pass)
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param prices:
        :return:
        """
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += (prices[i] - prices[i - 1])
        return profit

    def max_profit_(self, prices: List[int]) -> int:
        """
        Approach: Peak Valley
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param prices:
        :return:
        """

        profit = day = 0
        total_days = len(prices) - 1

        while day < total_days:

            while day < total_days and prices[day] >= prices[day + 1]:
                day += 1
            valley = prices[day]
            while day < total_days and prices[day] < prices[day + 1]:
                day += 1
            peak = prices[day]

            profit += (peak - valley)
        return profit


if __name__ == "__main__":

    stock = Stock()
    print(stock.max_profit_([7, 1, 5, 3, 6, 4]))
    print(stock.max_profit([7, 1, 5, 3, 6, 4]))

