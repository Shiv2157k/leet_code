

class Grid:

    def get_unique_paths(self, m: int, n: int) -> int:
        """
        Approach: Recursion
        Time Complexity:
        Space Complexity:
        :param m:
        :param n:
        :return:
        """
        # base case
        if m == 1 or n == 1:
            return 1
        return self.get_unique_paths(m - 1, n) + self.get_unique_paths(m, n - 1)

    def get_unique_paths_(self, m: int, n: int) -> int:
        """
        Approach: Dynamic Programming
        Time Complexity: O(N * M)
        Space Complexity: O(N * M)
        :param m:
        :param n:
        :return:
        """
        paths = [[1] * n for _ in range(m)]
        for col in range(1, m):
            for row in range(1, n):
                paths[col][row] = paths[col - 1][row] + paths[col][row - 1]
        return paths[m - 1][n - 1]

    def get_unique_paths__(self, m: int, n: int) -> int:
        """
        Approach: Using math factorial.
        Time Complexity: O((M + N)(log(M + N)log log(M + N))^2)
        Space Complexity: O(1)
        :param m:
        :param n:
        :return:
        """
        from math import factorial
        return factorial(m + n - 2) // factorial(m - 1) // factorial(n - 1)


if __name__ == "__main__":
    grid = Grid()
    print(grid.get_unique_paths(7, 3))
    print(grid.get_unique_paths_(7, 3))
    print(grid.get_unique_paths__(7, 3))
