from typing import List
from collections import deque


class Islands:

    def total_number_bfs(self, grid: List[List[int]]) -> int:
        """
        Approach: BFS
        Time Complexity: O(M * N)
        Space Complexity: O(min(M,N))
        :param grid:
        :return:
        """
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        total_islands = 0
        q = deque()

        def bfs(grid: List[List[int]], q: "deque"):
            while q:
                row, col = q.popleft()
                for dr, dc in ((row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)):
                    if 0 <= dr < rows and 0 <= dc < cols and grid[dr][dc] == "1":
                        grid[dr][dc] = "0"
                        q.append((dr, dc))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    q.append((row, col))
                    grid[row][col] = "0"
                    bfs(grid, q)
                    total_islands += 1
        return total_islands

    def total_number_dfs(self, grid: List[List[int]]) -> int:
        """
        Approach: DFS
        Time Complexity: O(M * N)
        Space Complexity: O(M * N)
        :param grid:
        :return:
        """
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        total_islands = 0

        def dfs(row: int, col: int):
            if 0 <= row < rows and 0 <= col < cols and grid[row][col] == "1":
                grid[row][col] = 0
                dfs(row + 1, col)
                dfs(row - 1, col)
                dfs(row, col + 1)
                dfs(row, col - 1)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    total_islands += 1
                    dfs(row, col)
        return total_islands


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