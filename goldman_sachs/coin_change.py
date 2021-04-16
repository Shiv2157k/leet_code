from typing import List


class CoinChange:

    def minimum_coins(self, coins: List[int], amount: int) -> int:
        """
        Approach: DP
        Time Complexity: O(MN)
        Space Complexity: O(N)
        :param coins:
        :param amount:
        :return:
        """

        dp = [0] + [float("inf")] * amount

        for coin in coins:
            for a in range(coin, amount + 1):
                dp[a] = min(dp[a], 1 + dp[a - coin])
        return dp[-1] if dp[-1] != float("inf") else -1


if __name__ == "__main__":

    coin_change = CoinChange()
    print(coin_change.minimum_coins([1, 2, 5], 11))
    print(coin_change.minimum_coins([2], 5))