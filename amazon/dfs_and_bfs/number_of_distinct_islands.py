from typing import List


class Islands:

    def get_distinct_islands(self, grid: List[List[int]]) -> int:
        """
        Approach: Hash by path signature
        Time Complexity: O(MN)
        Space Complexity: O(MN)
        :param grid:
        :return:
        """
        rows, cols = len(grid), len(grid[0])
        distinct_islands = set()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    path = self.compute_path(row, col, grid, rows, cols, "X")
                    distinct_islands.add(path)
        return len(distinct_islands)

    def compute_path(self, row: int, col: int, grid: List[List[int]], rows: int, cols: int, route: str) -> str:
        """
        Computes the island shape.
        :param row:
        :param col:
        :param grid:
        :param rows:
        :param cols:
        :param route:
        :return:
        """
        # base case
        if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] == 0:
            return "O"

        # mark the grid to water once visited
        grid[row][col] = 0

        left = self.compute_path(row, col - 1, grid, rows, cols, "L")
        right = self.compute_path(row, col + 1, grid, rows, cols, "R")
        up = self.compute_path(row - 1, col, grid, rows, cols, "U")
        down = self.compute_path(row + 1, col, grid, rows, cols, "D")

        return route + left + right + up + down


if __name__ == "__main__":
    islands = Islands()
    print(islands.get_distinct_islands(
        [
            [1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1],
            [0, 0, 0, 1, 1]
        ]
    ))
    print(islands.get_distinct_islands(
        [
            [1, 1, 0, 1, 1],
            [1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1],
            [1, 1, 0, 1, 1]
        ]
    ))