from typing import List


class Grid:

    def get_minimum_path_sum(self, grid: List[List[int]]) -> int:
        """
        Approach: DP Bottom - Up
        Time Complexity: O(MN)
        Space Complexity: O(1)
        :param grid:
        :return:
        """
        rows, cols = len(grid), len(grid[0])

        for row in range(rows - 1, -1, -1):
            for col in range(cols - 1, -1, -1):
                # calculate the last vertical grid
                if row == rows - 1 and col != cols - 1:
                    grid[row][col] = grid[row][col] + grid[row][col + 1]
                # calculate the last horizontal grid
                elif row != rows - 1 and col == cols - 1:
                    grid[row][col] = grid[row][col] + grid[row + 1][col]
                # calculate the in b/w grids
                elif row != rows - 1 and col != cols - 1:
                    grid[row][col] = grid[row][col] + min(grid[row + 1][col], grid[row][col + 1])
        return grid[0][0]


if __name__ == "__main__":
    cells = Grid()
    print(cells.get_minimum_path_sum(
        [
            [1, 3, 1],
            [1, 5, 1],
            [4, 2, 1]
        ]
    ))