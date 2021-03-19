from typing import List
from collections import deque


class Matrix:

    def shortest_path(self, grid: List[List[int]]):
        """
        Approach: BFS
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param grid:
        :return:
        """
        rows, cols = len(grid), len(grid[0])
        q = deque()
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1), (-1, -1), (1, 1), (1, -1), (-1, 1)]

        if grid[0][0] == 0:
            q.append((1, (0, 0)))

        while q:
            steps, coordinates = q.popleft()
            x, y = coordinates
            # base case
            if (x, y) == (rows - 1, cols - 1):
                return steps
            for dx, dy in dirs:
                if 0 <= x + dx < rows and 0 <= y + dy < cols and grid[x + dx][y + dy] == 0:
                    q.append((steps + 1, (x + dx, y + dy)))
                    grid[x + dx][y + dy] = 1
        return -1


if __name__ == "__main__":
    matrix = Matrix()
    print(matrix.shortest_path(
        [
            [0, 0, 0],
            [1, 1, 0],
            [1, 1, 0]
        ]
    ))
    print(matrix.shortest_path(
        [
            [1, 0, 0],
            [1, 1, 0],
            [1, 1, 0]
        ]
    ))
    print(matrix.shortest_path(
        [
            [0, 1],
            [1, 0]
        ]
    ))
