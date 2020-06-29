from typing import List


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

    def get_unique_paths_with_obstacles(self, obstacle_grid: List[List[int]]) -> int:
        """
        Approach: Dynamic Programming.
        Time Complexity: O(m * n)
        Space Complexity: O(1)
        :param obstacle_grid:
        :return:
        """

        # base case
        if obstacle_grid[0][0] == 1:
            return 0

        m, n, obstacle_grid[0][0] = len(obstacle_grid), len(obstacle_grid[0]), 1
        for i in range(1, m):
            obstacle_grid[i][0] = int(obstacle_grid[i][0] == 0 and obstacle_grid[i - 1][0] == 1)
        for j in range(1, n):
            obstacle_grid[0][j] = int(obstacle_grid[0][j] == 0 and obstacle_grid[0][j - 1] == 1)

        for col in range(1, m):
            for row in range(1, n):
                if obstacle_grid[col][row] == 0:
                    obstacle_grid[col][row] = obstacle_grid[col - 1][row] + obstacle_grid[col][row - 1]
                else:
                    obstacle_grid[col][row] = 0
        return obstacle_grid[m - 1][n - 1]


if __name__ == "__main__":
    grid = Grid()
    print(grid.get_unique_paths(7, 3))
    print(grid.get_unique_paths_(7, 3))
    print(grid.get_unique_paths__(7, 3))
    print(grid.get_unique_paths_with_obstacles(
        [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]
    ))
