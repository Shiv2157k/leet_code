from typing import List


class ChessBoard:

    def knights_probability(self, N: int, k: int, r: int, c: int) -> float:
        """
        Approach: DP
        Time Complexity: O(N^2 * k)
        Space Complexity: O(N^2)
        :param N:
        :param k:
        :param r:
        :param c:
        :return:
        """

        """
        Intuition:
        Let f(r, c, k) be probability of being on square (r, c) after exactly k steps
        f(r, c, k) = 
            - 1, 0 <= r, c <= n - 1 and k = 0
            - dx, dy [f(r + dx)(c + dy)(k - 1)]/ 8, 0 <= r, c <= n - 1 and k > 1
        Algorithm:
        1. Create 2 matrices A1, A2 of size n * n
        2. Initialize A1[r][c] = 1 & rest of entries in both matrices with 0's.
        3. Perform k times:
            - update entries in A2 which can be reached with knight's move from
              modified entries in A1
            - reset A1, to zeros and witch b/w A1 & A2
        4 Summarize all entries in A1 and return result.
        """

        current = [[0] * N for _ in range(N)]
        # mark the current knight position with 1
        current[r][c] = 1

        # for each move
        for _ in range(k):
            # initialize next move
            next_move = [[0] * N for _ in range(N)]
            for r, row in enumerate(current):
                for c, val in enumerate(row):
                    for dr, dc in ((1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1)):
                        if 0 <= r + dr < N and 0 <= c + dc < N:
                            next_move[r + dr][c + dc] += val / 8.0
                current = next_move
        probability = 0.0
        # return sum(map(sum, current))
        for x in range(len(current)):
            for y in range(len(current[0])):
                probability += current[x][y]
        return probability


if __name__ == "__main__":
    chessboard = ChessBoard()
    print(chessboard.knights_probability(3, 2, 0, 0))

