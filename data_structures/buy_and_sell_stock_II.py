from typing import List


class BuyStock:

    def get_max_profit(self, prices: List[int]) -> int:
        """
        Approach: One Pass Approach.
        Time Complexity: O(n)
        Space Complexity: O(1)
        :param prices:
        :return:
        """
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit


if __name__ == "__main__":

    stock = BuyStock()
    print(stock.get_max_profit([7, 1, 3, 5, 6, 4, 7]))
