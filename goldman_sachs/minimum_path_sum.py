from typing import List


class Grid:

    def minimum_path_sum_2d(self, grid: List[List[int]]) -> int:
        """
        Approach: DP (2 D Array)
        Time Complexity: O(MN)
        Space Complexity: O(MN)
        :param grid:
        :return:
        """

        rows, cols = len(grid), len(grid[0])
        dp = [[0] * cols for _ in range(rows)]

        for row in range(rows - 1, -1, -1):
            for col in range(cols - 1, -1, -1):
                if row == rows - 1 and col != cols - 1:
                    dp[row][col] = grid[row][col] + dp[row][col + 1]
                elif row != rows - 1 and col == cols - 1:
                    dp[row][col] = grid[row][col] + dp[row + 1][col]
                elif row != rows - 1 and col != cols - 1:
                    dp[row][col] = grid[row][col] + min(dp[row][col + 1], dp[row + 1][col])
                else:
                    dp[row][col] = grid[row][col]
        return dp[0][0]

    def minimum_path_sum_1d(self, grid: List[List[int]]) -> int:
        """
        Approach: DP (1D Array)
        Time Complexity: O(MN)
        Space Complexity: O(N)
        :param grid:
        :return:
        """

        rows, cols = len(grid), len(grid[0])
        dp = [0] * cols

        for row in range(rows - 1, -1, -1):
            for col in range(cols - 1, -1, -1):
                if row == rows - 1 and col != cols - 1:
                    dp[col] = grid[row][col] + dp[col + 1]
                elif row != rows - 1 and col == cols - 1:
                    dp[col] = grid[row][col] + dp[col]
                elif row != rows - 1 and col != cols - 1:
                    dp[col] = grid[row][col] + min(dp[col], dp[col + 1])
                else:
                    dp[col] = grid[row][col]
        return dp[0]

    def minimum_path_sum_no_extra_space(self, grid: List[List[int]]) -> int:
        """
        Approach: DP (No extra space)
        Time Complexity: O(MN)
        Space Complexity: O(1)
        :param grid:
        :return:
        """

        rows, cols = len(grid), len(grid[0])

        for row in range(rows - 1, -1, -1):
            for col in range(cols - 1, -1, -1):
                if row == rows - 1 and col != cols - 1:
                    grid[row][col] = grid[row][col] + grid[row][col + 1]
                elif row != rows - 1 and col == cols - 1:
                    grid[row][col] = grid[row][col] + grid[row + 1][col]
                elif row != rows - 1 and col != cols - 1:
                    grid[row][col] = grid[row][col] + min(grid[row][col + 1], grid[row + 1][col])
        return grid[0][0]


if __name__ == "__main__":
    g = Grid()
    print(g.minimum_path_sum_1d(
        [
            [1, 3, 1], [1, 5, 1], [4, 2, 1]
        ]
    ))
    print(g.minimum_path_sum_2d(
        [
            [1, 3, 1], [1, 5, 1], [4, 2, 1]
        ]
    ))
    print(g.minimum_path_sum_no_extra_space(
        [
            [1, 3, 1], [1, 5, 1], [4, 2, 1]
        ]
    ))

