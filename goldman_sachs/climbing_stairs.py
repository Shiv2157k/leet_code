

class Stairs:

    def __init__(self):
        self.cache = {}

    def number_of_ways_to_climb(self, n: int) -> int:
        """
        Approach: Recursion + Memoization
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param n:
        :return:
        """
        if n in self.cache:
            return self.cache[n]

        if n == 0 or n == 1:
            val = 1
        else:
            val = self.number_of_ways_to_climb(n - 1) + self.number_of_ways_to_climb(n - 2)
        self.cache[n] = val
        return val

    def number_of_ways_to_climb_dp(self, n: int) -> int:
        """
        Approach: DP
        Time Complexity: O(N)
        Space Complexity:
        :param n:
        :return:
        """
        dp = {0: 1, 1: 1}
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

    def number_of_ways_to_climb_fibonacci(self, n) -> int:
        """
        Approach: Fibonacci Number
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param n:
        :return:
        """
        if n == 1:
            return 1
        first, second = 1, 2
        for i in range(3, n + 1):
            third = first + second
            first = second
            second = third
        return second


if __name__ == "__main__":

    stairs = Stairs()
    print(stairs.number_of_ways_to_climb(2))
    print(stairs.number_of_ways_to_climb(3))
    print(stairs.number_of_ways_to_climb(4))
    print(stairs.number_of_ways_to_climb(5))
    print("--------------------------------")
    print(stairs.number_of_ways_to_climb_dp(2))
    print(stairs.number_of_ways_to_climb_dp(3))
    print(stairs.number_of_ways_to_climb_dp(4))
    print(stairs.number_of_ways_to_climb_dp(5))
    print("----------------------------------")
    print(stairs.number_of_ways_to_climb_fibonacci(2))
    print(stairs.number_of_ways_to_climb_fibonacci(3))
    print(stairs.number_of_ways_to_climb_fibonacci(4))
    print(stairs.number_of_ways_to_climb_fibonacci(5))