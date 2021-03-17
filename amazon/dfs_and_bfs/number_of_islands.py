from typing import List
from collections import deque


class Islands:

    def total_number_bfs(self, grid: List[List[str]]) -> int:
        """
        Approach: BFS
        Time Complexity: O(MN)
        Space Complexity: O(min(MN))
        :param grid:
        :return:
        """
        if not grid:
            return 0
        number_of_islands = 0
        rows, cols = len(grid), len(grid[0])
        q = deque()

        def helper(grid, q):
            while q:
                row, col = q.popleft()
                for dr, dc in ((row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)):
                    if 0 <= dr < len(grid) and 0 <= dc < len(grid[0]) and grid[dr][dc] == "1":
                        q.append((dr, dc))
                        grid[dr][dc] = "0"

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    grid[row][col] = "0"
                    q.append((row, col))
                    helper(grid, q)
                    number_of_islands += 1
        return number_of_islands

    def total_number_dfs(self, grid: List[List[str]]) -> int:
        """
        Approach: DFS
        Time Complexity: O(MN)
        Space Complexity: O(MN)
        :param grid:
        :return:
        """
        # validation
        if not grid:
            return 0
        number_of_islands = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(grid, row, col):
            # base case
            if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] != "1":
                return
            grid[row][col] = "0"
            dfs(grid, row + 1, col)
            dfs(grid, row - 1, col)
            dfs(grid, row, col + 1)
            dfs(grid, row, col - 1)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    number_of_islands += 1
                    dfs(grid, row, col)
        return number_of_islands


if __name__ == "__main__":
    islands = Islands()
    print(islands.total_number_dfs(
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]
    ))
    print(islands.total_number_dfs(
        [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]
    ))
    print(islands.total_number_bfs(
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]
    ))
    print(islands.total_number_bfs(
        [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]
    ))
