from typing import List


class Stock:

    def maximum_profit(self, prices: List[int]) -> int:
        """
        Approach: Greedy (One Pass)
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param prices:
        :return:
        """

        max_profit, min_price = float("-inf"), float("inf")

        for price in prices:

            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit


if __name__ == "__main__":
    stock = Stock()
    print(stock.maximum_profit([7, 1, 5, 3, 6, 4]))