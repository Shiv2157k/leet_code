from typing import List


class Matrix:

    def set_to_zero(self, grid: List[List[int]]) -> int:
        """
        Approach: Space Optimization
        Time Complexity: O(M * N)
        Space Complexity: O(1)
        :param grid:
        :return:
        """

        is_col = False
        rows, cols = len(grid), len(grid[0])

        for row in range(rows):
            if grid[row][0] == 0:
                is_col = True
            for col in range(1, cols):
                if grid[row][col] == 0:
                    grid[row][0] = 0
                    grid[0][col] = 0

        for row in range(1, rows):
            for col in range(1, cols):
                if not grid[row][0] or not grid[0][col]:
                    grid[row][col] = 0

        if grid[0][0] == 0:
            for col in range(cols):
                grid[0][col] = 0

        if is_col:
            for row in range(rows):
                grid[row][0] = 0

        return grid

    def set_to_zero_(self, grid: List[List[int]]) -> int:
        """
        Approach: Using Set
        Time Complexity: O(M * N)
        Space Complexity : O(N)
        :param grid:
        :return:
        """
        row_set, col_set = set(), set()

        rows, cols = len(grid), len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    row_set.add(row)
                    col_set.add(col)

        for row in range(rows):
            for col in range(cols):
                if row in row_set or col in col_set:
                    grid[row][col] = 0
        return grid


if __name__ == "__main__":
    matrix = Matrix()
    print(matrix.set_to_zero([
        [1, 1, 1], [1, 0, 1], [1, 1, 1]
    ]))
    print(matrix.set_to_zero_([
        [1, 1, 1], [1, 0, 1], [1, 1, 1]
    ]))
