from typing import List


class Stock:

    def best_time_to_buy_and_sell_stock(self, prices: List[int]) -> int:
        """
        Approach: One Pass
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param prices:
        :return:
        """
        low_price, max_profit = float("inf"), 0

        for price in prices:
            low_price = min(low_price, price)
            max_profit = max(max_profit, price - low_price)
        return max_profit


if __name__ == "__main__":
    stock = Stock()
    print(stock.best_time_to_buy_and_sell_stock([7, 1, 5, 3, 6, 4]))
    print(stock.best_time_to_buy_and_sell_stock([7, 6, 4, 3, 1]))