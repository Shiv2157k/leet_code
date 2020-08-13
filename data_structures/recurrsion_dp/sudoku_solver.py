from typing import List

from collections import defaultdict


class Sudoku:

    def solve(self, board: List[List[str]]) -> List[List[str]]:
        """
        Approach: Back Tracking
        Time Complexity: O(N!)
        Space Complexity: O(N)
        :param board:
        :return:
        """

        def could_place(d: int, row: int, col: int) -> bool:
            """
            Returns the boolean if we can place the number in a particular cell.
            :param d:
            :param row:
            :param col:
            :return:
            """
            return not (d in rows[row] or d in columns[col] or d in boxes[box_index(row, col)])

        def place_number(d: int, row: int, col: int):
            """
            Places the number in to the cell.
            :param d:
            :param row:
            :param col:
            :return:
            """
            rows[row][d] += 1
            columns[col][d] += 1
            boxes[box_index(row, col)][d] += 1
            board[row][col] = str(d)

        def remove_number(d: int, row: int, col: int):
            """
            Removes the number from a cell.
            :param d:
            :param row:
            :param col:
            :return:
            """
            del rows[row][d]
            del columns[col][d]
            del boxes[box_index(row, col)][d]
            board[row][col] = "."

        def place_next_numbers(row: int, col: int):
            """
            Places the next numbers into the next cell.
            If reached the end and found thr solution
            We mark it as solved.
            :param row:
            :param col:
            :return:
            """
            if row == N - 1 and col == N - 1:
                nonlocal sudoku_solved
                sudoku_solved = True
            else:
                if col == N - 1:
                    back_track(row + 1, 0)
                else:
                    back_track(row, col + 1)

        def back_track(row=0, col=0):
            """
            Back tracks the entire boards.
            :param row:
            :param col:
            :return:
            """
            if board[row][col] == ".":
                for d in range(1, 10):
                    if could_place(d, row, col):
                        place_number(d, row, col)
                        place_next_numbers(row, col)
                        if not sudoku_solved:
                            remove_number(d, row, col)
            else:
                place_next_numbers(row, col)

        n = 3
        N = n * n
        # Function used to calculate and get the box index.
        box_index = lambda row, col: (row // n) * n + col // n
        rows = [defaultdict(int) for _ in range(N)]
        columns = [defaultdict(int) for _ in range(N)]
        boxes = [defaultdict(int) for _ in range(N)]

        for i in range(N):
            for j in range(N):
                if board[i][j] != ".":
                    d = int(board[i][j])
                    place_number(d, i, j)

        sudoku_solved = False
        back_track()
        return board, sudoku_solved


if __name__ == "__main__":
    sudoku = Sudoku()
    print(sudoku.solve(
        [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"]
        ]
    ))
