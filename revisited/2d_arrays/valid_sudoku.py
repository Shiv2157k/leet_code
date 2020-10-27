from typing import List


class Sudoku:

    def is_valid(self, board: List[List[int]]) -> bool:
        """
        Approach: One Iteration
        Time Complexity: O(1)
        Space Complexity: O(1)
        Formulae for box index:
        box_index = (row // 3) * 3 + col // 3
        :param board:
        :return:
        """
        matrix = len(board[0])
        rows = [{} for _ in range(matrix)]
        cols = [{} for _ in range(matrix)]
        boxes = [{} for _ in range(matrix)]

        for row in range(matrix):
            for col in range(matrix):
                num = board[row][col]
                if num != ".":
                    num = int(num)
                    box_idx = (row // 3) * 3 + col // 3
                    rows[row][num] = rows[row].get(num, 0) + 1
                    cols[col][num] = cols[col].get(num, 0) + 1
                    boxes[box_idx][num] = boxes[box_idx].get(num, 0) + 1

                    if rows[row][num] > 1 or cols[col][num] > 1 or boxes[box_idx][num] > 1:
                        return False
        return True


if __name__ == "__main__":
    sudoku = Sudoku()
    print(sudoku.is_valid(
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
    print(sudoku.is_valid(
        [
            ["5", "3", "3", ".", "7", ".", ".", ".", "."],
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
