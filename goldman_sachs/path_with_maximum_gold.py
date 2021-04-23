from typing import List


class Gold:

    def get_max(self, grid: List[List[int]]) -> int:
        """
        Approach: Back Tracking
        Time Complexity:  O((k*4^k) + mn)
        Space Complexity: O(1)
        :param grid:
        :return:
        """

        rows, cols = len(grid), len(grid[0])
        curr_sum = max_sum = 0

        def back_track(r: int, c: int):
            """
            :param r:
            :param c:
            :return:
            """
            nonlocal curr_sum, max_sum
            found = True
            for dr, dc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if 0 <= dr < rows and 0 <= dc < cols and 0 < grid[dr][dc]:
                    found = False

                    v = grid[dr][dc]

                    curr_sum += v

                    grid[dr][dc] = 0

                    back_track(dr, dc)
                    curr_sum -= v
                    grid[dr][dc] = v
            if found:
                max_sum = max(max_sum, curr_sum)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] != 0:
                    value = curr_sum = grid[row][col]
                    grid[row][col] = 0
                    back_track(row, col)
                    grid[row][col] = value
        return max_sum


if __name__ == "__main__":
    gold = Gold()
    print(gold.get_max(
        [
            [0, 6, 0],
            [5, 8, 7],
            [0, 9, 0]
        ]
    ))