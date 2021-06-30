from typing import List


class WordSearch:

    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Approach: Back Tracking
        N - length of the grid
        L - Number of letters in the word
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
        """

        :param row
        :param col
        :param suffix
        :return
        """

        # base case
        # if we have reached end of the suffix
        # we have traversed all the words
        # which means there is a word that exists
        if len(suffix) == 0:
            return True

        # edge cases
        if row < 0 or row == self.ROWS or col < 0 or col == self.COLS or self.board[row][col] != suffix[0]:
            return False

        # mark the current starting point
        self.board[row][col] = "#"

        for dr, dc in ((row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)):
            if self.back_track(dr, dc, suffix[1:]):
                return True

        # un-mark the current starting point
        self.board[row][col] = suffix[0]
        return False


if __name__ == "__main__":
    word_search = WordSearch()
    print(word_search.exist(
        board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCCED"
    ))
    print(word_search.exist(
        board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="SEE"
    ))
    print(word_search.exist(
        board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCB"
    ))
