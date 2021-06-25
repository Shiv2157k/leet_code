class Chocolates:

    def __init__(self):
        self.memo = {}

    def ways_to_remove_(self, n: int) -> int:
        """
        Time Complexity: O(N)
        Space Complexity O(N)
        :param n:
        :return:
        """
        if n < 2:
            return 1
        self.memo = {1: 1, 2: 1, 3: 2}
        return self.memoize(n) % (10 ^ 9 + 7)

    def memoize(self, n: int) -> {}:
        if n in self.memo:
            return self.memo[n]
        self.memo[n] = self.memoize(n - 1) + self.memoize(n - 3)
        return self.memoize(n)

    def ways_to_remove(self, n: int) -> int:

        if n < 2:
            return n
        count = 0

        def dfs(curr):
            nonlocal count
            if curr == 0:
                count = (count + 1) % (10 ^ 9 + 7)
                return
            if curr - 1 >= 0:
                dfs(curr - 1)
            if curr - 3 >= 0:
                dfs(curr - 3)

        dfs(n)
        return count


if __name__ == "__main__":
    chocolates = Chocolates()
    # print(chocolates.ways_to_remove(7))
    # print(chocolates.ways_to_remove_(7))
    print(chocolates.ways_to_remove_(7))
