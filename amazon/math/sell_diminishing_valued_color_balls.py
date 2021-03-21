from typing import List


class Balls:

    def max_profit(self, inventory: List[int], orders: int) -> int:
        """
        Approach: Arithmetic Expression
        Formuale:
        n * (n + 1) / 2 - (k * (k + 1)) / 2
        k = factor
        Time Complexity: O(N log N)
        Space Complexity: O(1)
        :param inventory:
        :param orders:
        :return:
        """
        def get_sum(start, end):
            return start * (start + 1) // 2 - end * (end + 1) // 2

        inventory.sort(reverse=True)
        n = len(inventory)
        i = profit = 0
        # how many colors have same amount
        factor = 1
        while orders > 0:
            # if we can make sale for all factor
            if i < n - 1 and inventory[i] > inventory[i + 1] and orders >= factor * (inventory[i] - inventory[i + 1]):
                orders_taken = factor * (inventory[i] - inventory[i + 1])
                curr_profit = factor * get_sum(inventory[i], inventory[i + 1])
                profit += curr_profit
                orders -= orders_taken
            # if we cannot make sale for all factors
            # or reached end
            elif i == n - 1 or inventory[i] > inventory[i + 1]:
                sell_all, rem_orders = orders // factor, orders % factor
                curr_profit = factor * get_sum(inventory[i], inventory[i] - sell_all)
                profit += curr_profit
                profit += rem_orders * (inventory[i] - sell_all)
                break
            i += 1
            factor += 1
        return profit % (10**9 + 7)


if __name__ == "__main__":
    balls = Balls()
    print(balls.max_profit(
        [2, 5], 4
    ))
    balls = Balls()
    print(balls.max_profit(
        [3, 5], 6
    ))
