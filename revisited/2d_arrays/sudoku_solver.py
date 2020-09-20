from typing import List
from collections import defaultdict
from pprint import pprint


class Sudoku:

    def solve(self, board: List[List[int]]):
        """
        Approach: Back Tracking.
        :param board:
        :return:
        """

        def could_be_placed(num: int, row: int, col: int) -> bool:
            """
            Verifies if the provided number can be placed or not.
            :param num:
            :param row:
            :param col:
            :return:
            """
            return not (num in rows[row] or num in cols[col] or num in boxes[box_index(row, col)])

        def place_number(num: int, row: int, col: int):
            """
            Place a number num in (row, col) cell.
            :param num:
            :param row:
            :param col:
            :return:
            """
            rows[row][num] += 1
            cols[col][num] += 1
            boxes[box_index(row, col)][num] += 1
            board[row][col] = str(num)

        def remove_number(num: int, row: int, col: int):
            """
            Remove a number which didn't lead to a solution.
            :param num:
            :param row:
            :param col:
            :return:
            """
            del rows[row][num]
            del cols[col][num]
            del boxes[box_index(row, col)][num]
            board[row][col] = "."

        def place_next_numbers(row: int, col: int):
            """
            Call back track function in recursion to continue
            to place numbers till the moment we have a solution.
            :param row:
            :param col:
            :return:
            """
            # if we are in the last cell
            # that means we have solution.
            if row == N - 1 and col == N - 1:
                nonlocal sudoku_solved
                sudoku_solved = True
            else:  # if not yet
                # if we're in end of row go to next row.
                if col == N - 1:
                    back_track(row + 1, 0)
                else:  # go to next column
                    back_track(row, col + 1)

        def back_track(row=0, col=0):
            """
            Back tracking.
            :param row:
            :param col:
            :return:
            """
            # if the cell is empty
            if board[row][col] == ".":
                # iterate over all numbers from 1 to 9.
                for num in range(1, 10):
                    if could_be_placed(num, row, col):
                        place_number(num, row, col)
                        place_next_numbers(row, col)
                        # if sudoku is solved, there is no need to back track.
                        # Since the single unique solution is what we wanted.
                        if not sudoku_solved:
                            remove_number(num, row, col)
            else:
                place_next_numbers(row, col)

        # box size
        n = 3
        # row size
        N = n * n
        # generates box indexes
        box_index = lambda row, col: (row // n) * n + col // n

        # initialize rows, columns and boxes.
        rows = [defaultdict(int) for _ in range(N)]
        cols = [defaultdict(int) for _ in range(N)]
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
    pprint(sudoku.solve(
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
