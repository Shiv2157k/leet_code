

class ChessBoard:

    def knights_probability(self, size: int, moves: int, row: int, col: int) -> int:
        """
        Approach: DP
        Time Complexity: O(N^2 * K)
        Space Complexity: O(N^2)
        Recursion Formulae:
        f[r + dr] + f[c + dc] + (moves - 1) / 8.0
        :param size:
        :param moves:
        :param row:
        :param col:
        :return:
        """
        board = [[0] * size for _ in range(size)]
        # starting point
        board[row][col] = 1

        # first outer loop iterate with moves
        for _ in range(moves):
            # another 2d array to store next moves probability
            next_move = [[0] * size for _ in range(size)]
            for r, curr_row in enumerate(board):
                for c, val in enumerate(curr_row):
                    # loop through the directions and calculate the probability
                    for dr, dc in ((2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)):
                        if 0 <= r + dr < size and 0 <= c + dc < size:
                            next_move[r + dr][c + dc] += val / 8.0
            board = next_move
        return sum(map(sum, board))


if __name__ == "__main__":
    chess_board = ChessBoard()
    print(chess_board.knights_probability(3, 2, 0, 0))
