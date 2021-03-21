from typing import List
from collections import deque


class Oranges:

    def minutes_took_for_all_to_rot(self, grid: List[int]) -> int:
        """
        Approach: BFS
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param grid:
        :return:
        """
        rows, cols = len(grid), len(grid[0])

        fresh_oranges = 0
        # initialize with -1, -1 as delimiter
        q = deque()

        # step 1: loop through count all the fresh oranges
        # and add all the grids containing rotten oranges
        # into queue
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    q.append((row, col))
                elif grid[row][col] == 1:
                    fresh_oranges += 1

        # mark the round / level i.e., time stamp
        q.append((-1, -1))

        # steps 2: start the rotting process
        minutes_elapsed = -1
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while q:
            row, col = q.popleft()
            if row == -1:
                # we finished round processing
                minutes_elapsed += 1
                if q:  # to avoid endless loop
                    q.append((-1, -1))
            else:
                for r, c in directions:
                    dr, dc = row + r, col + c
                    if rows > dr >= 0 and cols > dc >= 0:
                        if grid[dr][dc] == 1:
                            # rot this orange
                            grid[dr][dc] = 2
                            fresh_oranges -= 1
                            q.append((dr, dc))
        return minutes_elapsed if not fresh_oranges else -1


if __name__ == "__main__":
    O = Oranges()
    print(O.minutes_took_for_all_to_rot(
        [
            [2, 1, 1],
            [1, 1, 0],
            [0, 1, 1]
        ]
    ))
    print(O.minutes_took_for_all_to_rot(
        [
            [2, 1, 1],
            [0, 1, 1],
            [1, 0, 1]
        ]
    ))
