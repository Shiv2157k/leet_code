from typing import List


class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.row = [0] * n
        self.col = [0] * n
        self.diagonal = [0] * 2


    def move(self, row: int, col: int, player: int) -> int:

        if player == 1:
            self.row[row] += 1
            self.col[col] += 1
            if row == col:
                self.diagonal[0] += 1
            if row + col == self.n - 1:
                self.diagonal[1] += 1
            if self.row[row] == self.n or self.col[col] == self.n or self.diagonal[0] == self.n or self.diagonal[1] == self.n:
                return 1
        else:
            self.row[row] -= 1
            self.col[col] -= 1
            if row == col:
                self.diagonal[0] -= 1
            if row + col == self.n - 1:
                self.diagonal[1] -= 1
            if self.row[row] == -self.n or self.col[col] == -self.n or self.diagonal[0] == -self.n or self.diagonal[1] == -self.n:
                return 2
        return 0


if __name__ == "__main__":
    tic_tac_toe = TicTacToe(3)
    print(tic_tac_toe.move(0, 0, 1))
    print(tic_tac_toe.move(0, 2, 2))
    print(tic_tac_toe.move(2, 2, 1))
    print(tic_tac_toe.move(1, 1, 2))
    print(tic_tac_toe.move(2, 0, 1))
    print(tic_tac_toe.move(1, 0, 2))
    print(tic_tac_toe.move(2, 1, 1))
