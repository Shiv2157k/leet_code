from typing import List


class Word:

    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Approach: Back tracking.
        Time Complexity: O(N * 4^L)
        Space Complexity: O(L)
        :param board:
        :param word:
        :return:
        """
        # get number of rows and columns
        rows = len(board)
        cols = len(board[0])
        # loop through to find the first word and continue until the end.
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0] and self.dfs(board, row, col, 0, word):
                    return True
        return False

    def dfs(self, board: List[List[str]], row: int, col: int, count: int, word: str):

        # base case
        if count == len(word):
            return True
        # edge case
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != word[count]:
            return False

        # mark the current grid
        value = board[row][col]
        board[row][col] = "#"

        # check all directions from the current grid.
        found = self.dfs(board, row + 1, col, count + 1, word) or \
                self.dfs(board, row, col + 1, count + 1, word) or \
                self.dfs(board, row - 1, col, count + 1, word) or \
                self.dfs(board, row, col - 1, count + 1, word)
        # assign the grid value back
        board[row][col] = value
        return found

    def exist_(self, board: List[List[str]], word: str) -> bool:
        """
        Approach: Back tracking
        Time Complexity: O(N * 4^L)
        Space Complexity: O(L)
        :param board:
        :param word:
        :return:
        """
        self.ROWS = len(board)
        self.COLS = len(board[0])
        self.board = board

        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.back_track(row, col, word):
                    return True
        return False

    def back_track(self, row: int, col: int, suffix: str) -> bool:

        # base cases
        if len(suffix) == 0:
            return True
        # edge cases
        if row < 0 or row >= self.ROWS or col < 0 or col >= self.COLS or self.board[row][col] != suffix[0]:
            return False

        # mark the grid
        self.board[row][col] = "#"
        found = False
        # explore in all the directions
        for row_offset, col_offset in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            found = self.back_track(row + row_offset, col + col_offset, suffix[1:])
            # if found break the loop.
            if found:
                break
        self.board[row][col] = suffix[0]
        return found


if __name__ == "__main__":
    word = Word()
    print(word.exist(
        [
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"]
        ], "ABCCED"
    ))
    print(word.exist(
        [
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"]
        ], "ABCED"
    ))
    print(word.exist_(
        [
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"]
        ], "ABCCED"
    ))
    print(word.exist_(
        [
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"]
        ], "ABCED"
    ))

