from typing import List


class Stock:

    def get_profit(self, prices: List[int]) -> int:
        """
        Approach: One Pass (Greedy)
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param prices:
        :return:
        """
        low_price, profit = float("inf"), 0

        for price in prices:
            low_price = min(price, low_price)
            profit = max(profit, price - low_price)
        return profit


if __name__ == "__main__":
    stock = Stock()
    print(stock.get_profit([7, 1, 5, 3, 6, 4]))