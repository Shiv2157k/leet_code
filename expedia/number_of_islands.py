from typing import List
from collections import deque


class Islands:

    def total_number_(self, grid: List[List[str]]) -> int:
        """
        Approach: DFS
        Time Complexity: O(M * N)
        Space Complexity: O(M * N)
        :param grid:
        :return:
        """

        def dfs(row: int, col: int, grid: List[List[str]]):

            if 0 <= row < rows and 0 <= col < cols and grid[row][col] == "1":
                grid[row][col] = "0"
                dfs(row + 1, col, grid)
                dfs(row - 1, col, grid)
                dfs(row, col + 1, grid)
                dfs(row, col - 1, grid)

        rows, cols = len(grid), len(grid[0])
        total = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    total += 1
                    dfs(row, col, grid)
        return total

    def total_number(self, grid: List[List[int]]) -> int:
        """
        Approach: BFS
        Time Complexity: O(M * N)
        Space Complexity:O (min (M,N))
        :param grid:
        :return:
        """

        def helper(grid: List[List[str]], q: deque):

            while q:
                r, c = q.popleft()
                for dr, dc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    if 0 <= dr < rows and 0 <= dc < cols and grid[dr][dc] == "1":
                        q.append((dr, dc))
                        grid[dr][dc] = "0"

        rows, cols = len(grid), len(grid[0])
        total = 0
        q = deque()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    grid[row][col] = "0"
                    q.append((row, col))
                    helper(grid, q)
                    total += 1
        return total


if __name__ == "__main__":
    islands = Islands()
    print(islands.total_number(
        [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]
    ))
    print(islands.total_number_(
        [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]
    ))
