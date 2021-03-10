from typing import List
from collections import deque


class Oranges:

    def all_rotten_minutes(self, grid: List[List[int]]) -> int:
        """
        Approach: BFS
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param grid:
        :return:
        """

        rows, cols = len(grid), len(grid[0])
        fresh_oranges = 0
        q = deque()

        # step 1: store all the current rotten grid
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    q.append((row, col))
                elif grid[row][col] == 1:
                    fresh_oranges += 1
        # mark the round in queue
        q.append((-1, -1))
        minutes_elapsed = -1
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        while q:
            row, col = q.popleft()
            # if reached a round:
            if row == -1:
                # update the minutes elapsed
                minutes_elapsed += 1
                # add the marker for infinite loop
                if q:
                    q.append((-1, -1))
            else:
                for r, c in directions:
                    nr, nc = row + r, col + c
                    if rows > nr >= 0 and cols > nc >= 0:
                        if grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            fresh_oranges -= 1
                            q.append((nr, nc))
        return minutes_elapsed if fresh_oranges == 0 else -1


if __name__ == "__main__":
    oranges = Oranges()
    print(oranges.all_rotten_minutes(
        [
            [2, 1, 1],
            [1, 1, 0],
            [0, 1, 1]
        ]
    ))

    print(oranges.all_rotten_minutes(
        [
            [2, 1, 1],
            [0, 1, 1],
            [1, 0, 1]
        ]
    ))
