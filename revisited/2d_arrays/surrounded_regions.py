from typing import List
from itertools import product, chain
from collections import deque
from pprint import pprint


class SurroundedRegion:

    def capture(self, board: [List[List[str]]]) -> List[List[str]]:
        """
        Approach: BFS and DFS
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param board:
        :return:
        """
        # base case
        if not board or not board[0]:
            return

        self.ROWS = len(board)
        self.COLS = len(board[0])

        # Step 1: get the borders
        borders = chain(product(range(self.ROWS), [0, self.COLS - 1]),
                        product([0, self.ROWS - 1], range(self.COLS)))

        # Step 2: mark the borders with "$"
        for row, col in borders:
            self.breadth_first_search(board, row, col)
            # self.depth_first_search(board, row, col)
            # self.depth_first_search_(board, row, col)

        # Step 3: Capture the internal regions and flip the marked region to "O"
        for r in range(self.ROWS):
            for c in range(self.COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "$":
                    board[r][c] = "O"
        return board

    def depth_first_search(self, board: List[List[str]], row: int, col: int):

        # base cases
        if row < 0 or row >= self.ROWS or col < 0 or col >= self.COLS:
            return
        if board[row][col] != "O":
            return

        board[row][col] = "$"

        for r, c in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            self.depth_first_search(board, row + r, col + c)

    def depth_first_search_(self, board: List[List[str]], row: int, col: int):
        # base case
        if board[row][col] != "O":
            return

        board[row][col] = "$"

        if col < self.COLS - 1:
            self.depth_first_search_(board, row, col + 1)
        if row < self.COLS - 1:
            self.depth_first_search_(board, row + 1, col)
        if col > 0:
            self.depth_first_search_(board, row, col - 1)
        if row > 0:
            self.depth_first_search_(board, row - 1, col)

    def breadth_first_search(self, board: List[List[str]], row: int, col: int):

        queue = deque([(row, col)])
        while queue:
            (row, col) = queue.popleft()
            if board[row][col] != "O":
                continue
            board[row][col] = "$"

            if col < self.COLS - 1:
                queue.append((row, col + 1))
            if row < self.ROWS - 1:
                queue.append((row + 1, col))
            if col > 0:
                queue.append((row, col - 1))
            if row > 0:
                queue.append((row - 1, col))


if __name__ == "__main__":
    region = SurroundedRegion()
    pprint(region.capture(
        [
            ["X", "X", "X", "X"],
            ["X", "O", "O", "X"],
            ["X", "X", "O", "X"],
            ["X", "O", "X", "X"]
        ]))
    pprint(region.capture(
        [
            ["X", "X", "X", "X"],
            ["X", "O", "O", "X"],
            ["X", "X", "O", "X"],
            ["X", "O", "X", "X"]
        ]))