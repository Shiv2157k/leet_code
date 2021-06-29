

class ClimbingStairs:

    def __init__(self):
        self.memo = {}

    def distinct_ways(self, n: int) -> int:
        """
        Approach: Fibonacci Number
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param n:
        :return:
        """
        if n < 2:
            return 1

        first = 1
        second = 1

        for i in range(2, n + 1):
            third = first + second
            first = second
            second = third
        return second

    def distinct_ways_(self, n: int) -> int:
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

    def distinct_ways__(self, n: int) -> int:
        """
        Approach: Recursion with memoization
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param n:
        :return:
        """
        if n in self.memo:
            return self.memo[n]

        if n < 2:
            val = 1
        else:
            val = self.distinct_ways__(n - 1) + self.distinct_ways__(n - 2)

        self.memo[n] = val
        return val


if __name__ == "__main__":
    climbing_stairs = ClimbingStairs()
    print(climbing_stairs.distinct_ways__(n=3))
    print(climbing_stairs.distinct_ways__(n=4))
    print(climbing_stairs.distinct_ways__(n=5))
    print("X--------------------------------X")
    print(climbing_stairs.distinct_ways_(n=3))
    print(climbing_stairs.distinct_ways_(n=4))
    print(climbing_stairs.distinct_ways_(n=5))
    print("X--------------------------------X")
    print(climbing_stairs.distinct_ways(n=3))
    print(climbing_stairs.distinct_ways(n=4))
    print(climbing_stairs.distinct_ways(n=5))

