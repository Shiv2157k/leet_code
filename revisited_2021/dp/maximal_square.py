from typing import List


class Square:

    def maximal_area_(self, matrix: List[List[str]]) -> int:
        """
        Approach: DP (1D Array)
        Time Complexity: O(MN)
        Space Complexity: O(N)
        :param matrix:
        :return:
        """
        rows, cols = len(matrix), len(matrix[0])
        dp = [0] * (cols + 1)
        max_len = prev = 0

        for row in range(1, rows + 1):
            for col in range(1, cols + 1):
                temp = dp[col]
                if matrix[row - 1][col - 1] == "1":
                    dp[col] = min(prev, dp[col - 1], dp[col]) + 1
                    max_len = max(max_len, dp[col])
                prev = temp
        return max_len**2

    def maximal_area(self, matrix: List[List[str]]) -> int:
        """
        Approach: DP (2D Array)
        Time Complexity: O(MN)
        Space Complexity: O(MN)
        :param matrix:
        :return:
        """
        rows, cols = len(matrix), len(matrix[0])
        max_len = 0
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]

        for row in range(1, rows + 1):
            for col in range(1, cols + 1):
                if matrix[row - 1][col - 1] == "1":
                    dp[row][col] = 1 + min(dp[row - 1][col - 1], dp[row][col - 1], dp[row - 1][col])
                    max_len = max(max_len, dp[row][col])
        return max_len ** 2


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
    print(square.maximal_area(
        [
            ["0", "1"],
            ["1", "0"]
        ]
    ))
    print(square.maximal_area(
        [
            ["0"]
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
    print(square.maximal_area_(
        [
            ["0", "1"],
            ["1", "0"]
        ]
    ))
    print(square.maximal_area_(
        [
            ["0"]
        ]
    ))
