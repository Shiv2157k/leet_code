from typing import List
from math import inf


class Stock:

    def get_profit(self, prices: List[int]) -> int:
        """
        Approach: One Pass Approach.
        Time Complexity: O(n)
        Space Complexity: O(1)
        :param prices:
        :return:
        """
        less_price, profit = float(inf), 0
        for price in prices:
            less_price, profit = min(less_price, price), max(profit, price - less_price)
        return profit


if __name__ == "__main__":
    stocks = Stock()
    print(stocks.get_profit([7, 2, 1, 9, 6, 4]))