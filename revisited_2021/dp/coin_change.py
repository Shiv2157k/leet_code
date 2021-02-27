from typing import List


class Coin:

    def minimum_change(self, coins: List[int], amount: int) -> int:
        """
        Approach: DP (1 D array)
        Time Complexity: O(C*A)
        Space Complexity: O(A)
        :param coins:
        :param amount:
        :return:
        """
        ca = [0] + [float("inf")] * amount
        for c in coins:
            for a in range(c, amount + 1):
                # min(exclude, include)
                ca[a] = min(ca[a], 1 + ca[a - c])
        return ca[-1] if ca[-1] != float("inf") else -1

    def minimum_change_(self, coins: List[int], amount: int) -> int:
        """
        Approach: DP (2 D array)
        Time Complexity: O(C*A)
        Space Complexity: O(C*A)
        :param coins:
        :param amount:
        :return:
                    amount
                 0 1 2 3 4 5 6
                |- - - - - - -
         coins 0|0 i i i i i i
               1|0 1 2 3 4 5 6
               2|0 1 1 2 2 3 3
               3|0 1 1 2 2 1 2| -> result
        """
        n = len(coins)
        ca = [[0] * (amount + 1) for _ in range(n + 1)]

        for i in range(1, amount + 1):
            ca[0][i] = float("inf")

        for c in range(1, n + 1):
            for a in range(1, amount + 1):
                # if the current amount is less
                # the current coin
                if coins[c - 1] > a:
                    ca[c][a] = ca[c-1][a]
                else:  # min(include, exclude)
                    ca[c][a] = min(1 + ca[c][a - coins[c - 1]], ca[c-1][a])
        return ca[-1][-1] if ca[-1][-1] != float("inf") else -1


if __name__ == "__main__":
    coin = Coin()
    print(coin.minimum_change([1, 2, 5], 6))
    print(coin.minimum_change_([1, 2, 5], 6))


