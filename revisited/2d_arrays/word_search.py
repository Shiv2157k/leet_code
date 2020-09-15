from typing import List


class WordSearch:

    def is_word_valid(self, board: List[List[str]], word: str) -> bool:
        """
        Approach: Back Tracking
        Time Complexity: O(N * 3^L)
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

        # base case
        if len(suffix) == 0:
            return True
        # edge cases
        if row < 0 or row == self.ROWS or col < 0 or col == self.COLS or self.board[row][col] != suffix[0]:
            return False

        # marking the first element
        self.board[row][col] = "$"

        # goes into top, left, right and bottom direction.
        for row_offset, col_offset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if self.back_track(row + row_offset, col + col_offset, suffix[1:]):
                return True
        # un marking the first element.
        self.board[row][col] = suffix[0]
        return False


if __name__ == "__main__":
    word_search = WordSearch()
    print(word_search.is_word_valid(
        [
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"]
        ], "ABCCED"
    ))