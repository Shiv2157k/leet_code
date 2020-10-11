

class ClimbingStairs:

    cache = {}

    def get_number_of_ways(self, steps: int) -> int:
        """
        Approach: Recursion with Memoization.
        Time Complexity:
        Space Complexity:
        :param steps:
        :return:
        """

        # base case
        if steps in self.cache:
            return self.cache[steps]

        if steps == 0 or steps == 1:
            val = 1
        else:
            val = self.get_number_of_ways(steps - 1) + self.get_number_of_ways(steps - 2)
        self.cache[steps] = val
        return val

    def get_number_of_ways_(self, steps: int) -> int:
        """
        Approach: DP
        Time Complexity:
        Space Complexity:
        :param steps:
        :return:
        """
        dp = {0: 1, 1: 1}
        for i in range(2, steps + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[steps]


if __name__ == "__main__":
    climbing_stairs = ClimbingStairs()
    print(climbing_stairs.get_number_of_ways(5))
    print(climbing_stairs.get_number_of_ways_(5))
    print(climbing_stairs.get_number_of_ways(4))
    print(climbing_stairs.get_number_of_ways_(4))
    print(climbing_stairs.get_number_of_ways(6))
    print(climbing_stairs.get_number_of_ways_(6))