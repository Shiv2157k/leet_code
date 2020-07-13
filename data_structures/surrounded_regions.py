from typing import List
from itertools import product, chain
from collections import deque


class Region:

    def surround(self, board: List[List[str]]) -> List[List[str]]:
        """
        Approach: Depth First Search and Breadth First Search.
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param board:
        :return:
        """

        # validation
        if not board or not board[0]:
            return

        self.ROWS = len(board)
        self.COLS = len(board[0])

        # step 1: get the boundaries
        borders = chain(product(range(self.ROWS), [0, self.COLS - 1]),
                        product([0, self.ROWS - 1], range(self.COLS)))

        # step 2: mark the borders with "O"
        for row, col in borders:
            # self.depth_first_search(board, row, col)
            # self.depth_first_search_(board, row, col)
            self.breadth_first_search(board, row, col)

        # step 3: flip the border $ -> O and inner O -> X
        for row in range(self.ROWS):
            for col in range(self.COLS):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "$":
                    board[row][col] = "O"

        return board

    def depth_first_search(self, board: List[List[str]], row: int, col: int):

        if board[row][col] != "O":
            return
        board[row][col] = "$"

        if col < self.ROWS - 1:
            self.depth_first_search(board, row + 1, col)
        if row < self.COLS - 1:
            self.depth_first_search(board, row, col + 1)
        if col > self.ROWS:
            self.depth_first_search(board, row - 1, col)
        if row > self.COLS:
            self.depth_first_search(board, row, col - 1)

    def depth_first_search_(self, board: List[List[str]], row: int, col: int):

        if row < 0 or row >= self.ROWS or col < 0 or col >= self.COLS:
            return

        if board[row][col] != "O":
            return

        board[row][col] = "$"
        for r, c in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            self.depth_first_search_(board, row + r, col + c)

    def breadth_first_search(self, board: List[List[str]], row: int, col: int):
        queue = deque([(row, col)])
        while queue:
            (row, col) = queue.popleft()
            if board[row][col] != "0":
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

    region = Region()
    print(region.surround(
        [
            ["X", "X", "X", "X"],
            ["X", "O", "O", "X"],
            ["X", "X", "O", "X"],
            ["X", "O", "X", "X"]
        ]
    ))