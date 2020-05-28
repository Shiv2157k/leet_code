from functools import lru_cache


class ClimbingStairs:

    climb_stair_cache = {}

    def get_ways(self, val: int) -> int:
        """
        Approach: Dynamic Programming
        :param val:
        :return:
        """
        cache = {0: 1, 1: 1}

        for i in range(2, val + 1):
            cache[i] = cache[i - 1] + cache[i - 2]
        return cache[val]

    def get_ways_(self, val: int) -> int:
        """
        Approach: Recursion and Memoization.
        :param val:
        :return:
        """
        if val in self.climb_stair_cache:
            return self.climb_stair_cache[val]

        if val == 0 or val == 1:
            return 1
        else:
            res = self.get_ways_(val - 1) + self.get_ways_(val - 2)
        self.climb_stair_cache[val] = res
        return res

    @lru_cache(maxsize=100)
    def get_ways__(self, val: int) -> int:
        """
        Approach: recursion and built in cache.
        :param val:
        :return:
        """
        if val == 0 or val == 1:
            return 1
        else:
            return self.get_ways__(val - 1) + self.get_ways__(val - 2)


if __name__ == "__main__":
    ways = ClimbingStairs()
    print(ways.get_ways(100))
    print(ways.get_ways_(100))
    print(ways.get_ways__(100))
    print(ways.get_ways_(5))
    print(ways.get_ways__(5))
    print(ways.get_ways_(5))