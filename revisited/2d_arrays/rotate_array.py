from typing import List


class TwoDArray:

    def rotate__(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        Approach: One Pass
        Time Complexity: O(N^2)
        Space Complexity: O(1)
        :param matrix:
        :return:
        """
        n = len(matrix[0])
        for r in range(n // 2 + n % 2):
            for c in range(n // 2):
                temp = matrix[n - 1 - c][r]
                matrix[n - 1 - c][r] = matrix[n - 1 - r][n - 1 - c]
                matrix[n - 1 - r][n - 1 - c] = matrix[c][n - 1 - r]
                matrix[c][n - 1 - r] = matrix[r][c]
                matrix[r][c] = temp
        return matrix

    def rotate_(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        Approach: Four Rectangle Rotate
        Time Complexity: O(N^2)
        Space Complexity: O(1)
        :param matrix:
        :return:
        """
        n = len(matrix[0])

        for r in range(n // 2 + n % 2):
            for c in range(n % 2):
                temp = [0] * 4
                row, col = r, c
                # capture the edges into temp
                for cell in range(4):
                    temp[cell] = matrix[row][col]
                    row, col = col, n - 1 - row
                # rotate the edges
                for cell in range(4):
                    matrix[row][col] = temp[(cell - 1) % 4]
                    row, col = col, n - 1 - row
        return matrix

    def rotate(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        Approach: Transpose and Reverse
        Time Complexity: O(N^2)
        Space Complexity: O(1)
        :param matrix:
        :return:
        """

        n = len(matrix[0])
        # perform transpose of matrix
        for r in range(n):
            for c in range(r, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        # reverse each col
        for col in range(n):
            matrix[col].reverse()
        return matrix


if __name__ == "__main__":
    matrix_arr = TwoDArray()
    print(matrix_arr.rotate(
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
    ))
    print(matrix_arr.rotate_(
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
    ))
    print(matrix_arr.rotate__(
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
    ))