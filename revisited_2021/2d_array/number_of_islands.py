from typing import List


class Islands:

    def total_number_(self, grid: List[List[str]]) -> str:
        """
        Approach: BFS
        Time Complexity: O(M*N)
        Space Complexity: O(min(M,N))
        :param grid:
        :return:
        """
        from collections import deque

        if not grid:
            return 0
        rows, cols, island_count = len(grid), len(grid[0]), 0
        q = deque([])

        def helper(grid: List[List[str]], q: "deque"):
            while q:
                r, c = q.popleft()
                for dr, dc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    if 0 <= dr < rows and 0 <= dc < cols and grid[dr][dc] == "1":
                        q.append((dr, dc))
                        grid[dr][dc] = "0"

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    island_count += 1
                    q.append((row, col))
                    helper(grid, q)
                    grid[row][col] = "0"
        return island_count

    def total_number(self, grid: List[List[str]]) -> str:
        """
        Approach: DFS/ Back tracking
        Time Complexity: O(M*N)
        Space Complexity: O(M*N)
        :param grid:
        :return:
        """
        if not grid:
            return 0
        rows, cols, island_count = len(grid), len(grid[0]), 0

        def back_track(grid: List[List[str]], row: int, col: int):
            # base case
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == "0":
                return # back track
            grid[row][col] = "0"
            back_track(grid, row - 1, col)
            back_track(grid, row + 1, col)
            back_track(grid, row, col - 1)
            back_track(grid, row, col + 1)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    island_count += 1
                    back_track(grid, row, col)
        return island_count


if __name__ == "__main__":
    islands = Islands()
    print(islands.total_number([
        ["1", "1", "1", "0", "0"],
        ["1", "1", "1", "0", "1"],
        ["0", "0", "0", "1", "0"]
    ]))
    print(islands.total_number_([
        ["1", "1", "1", "0", "0"],
        ["1", "1", "1", "0", "1"],
        ["0", "0", "0", "1", "0"]
    ]))