from typing import List


class GoldMine:

    def path_with_max_gold(self, grid: List[List[int]]) -> int:
        """
        Approach: Back tracking (DFS)
        Time Complexity:
        Space Complexity:
        :param grid:
        :return:
        """
        rows, cols = len(grid), len(grid[0])
        curr_sum = max_sum = 0

        def back_track(row: int, col: int):
            nonlocal curr_sum, max_sum
            found = True
            for r, c in [(row + 1, col), (row, col + 1), (row - 1, col), (row, col - 1)]:
                if 0 <= r < rows and 0 <= c < cols and 0 < grid[r][c]:
                    found = False
                    value = grid[r][c]
                    curr_sum += value
                    # mark as visited
                    grid[r][c] = 0
                    # back track
                    back_track(r, c)
                    # undo the calculation
                    curr_sum -= value
                    # un-mark
                    grid[r][c] = value
            if found:
                max_sum = max(max_sum, curr_sum)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] != 0:
                    value = curr_sum = grid[row][col]
                    grid[row][col] = 0  # mark as visited
                    # dfs
                    back_track(row, col)
                    # un - mark
                    grid[row][col] = value
        return max_sum


if __name__ == "__main__":
    gold_mine = GoldMine()
    print(gold_mine.path_with_max_gold([
        [0, 6, 0],
        [5, 8, 7],
        [0, 9, 0]
    ]))
