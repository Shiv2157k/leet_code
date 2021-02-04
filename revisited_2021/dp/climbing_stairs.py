

class ClimbingStairs:

    cache = {}

    def total_ways(self, n: int) -> int:
        """
        Approach: Fibonacci Number
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param n:
        :param int:
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

    def total_ways_(self, n: int) -> int:
        """
        Approach: DP
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param n:
        :return:
        """
        cache = {0: 1, 1: 1}
        for i in range(2, n + 1):
            cache[i] = cache[i - 1] + cache[i - 2]
        return cache[n]

    def total_ways__(self, n: int) -> int:
        """
        Approach: Recursion with memoization
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
            val = self.total_ways(n - 1) + self.total_ways(n - 2)
        self.cache[n] = val
        return val

    def total_ways___(self, n: int) -> int:
        """
        Approach: Recursion
        :param n:
        :return:
        """

        if n == 2 or n == 3:
            return n
        return self.total_ways__(n - 2) + self.total_ways__(n - 1)


if __name__ == "__main__":
    climbing_stairs = ClimbingStairs()
    climbing_stairs_1 = ClimbingStairs()
    climb_stairs = ClimbingStairs()
    print(climb_stairs.total_ways(6))
    print(climbing_stairs_1.total_ways_(6))
    print(climbing_stairs.total_ways_(6))