from typing import List


class Square:

    def maximal_area_(self, board: List[List[int]]) -> int:
        """
        Approach: DP (1D Array)
        Time Complexity: O(MN)
        Space Complexity: O(N)
        :param board:
        :return:
        """
        rows, cols = len(board), len(board[0])
        dp = [0] * (cols + 1)

        max_len = prev = 0

        for row in range(1, rows + 1):
            for col in range(1, cols + 1):
                temp = dp[col]
                if board[row - 1][col - 1] == "1":
                    dp[col] = min(min(dp[col], prev), dp[col - 1]) + 1
                    max_len = max(max_len, dp[col])
                else:
                    dp[col] = 0
                prev = temp
        return max_len**2

    def maximal_area(self, board: List[List[int]]) -> int:
        """
        Approach: DP (2D Array)
        Time Complexity: O(MN)
        Space Complexity: O(MN)
        :param board:
        :return:
        """
        max_area = 0
        rows, cols = len(board), len(board[0])
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]
        for row in range(1, rows + 1):
            for col in range(1, cols + 1):
                if board[row - 1][col - 1] == "1":
                    dp[row][col] = 1 + min(dp[row - 1][col - 1], dp[row][col - 1], dp[row - 1][col])
                    max_area = max(dp[row][col], max_area)
        return max_area**2


if __name__ == "__main__":
    square = Square()
    print(square.maximal_area(
        [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"]
        ]
    ))
    print(square.maximal_area_(
        [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"]
        ]
    ))
