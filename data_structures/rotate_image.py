from typing import List


class RotateImage:

    def to_90_degrees(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        Approach: Transpose and then reverse.
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        :param matrix:
        :return:
        """
        n = len(matrix[0])
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            matrix[i].reverse()
        return matrix

    def to_90_degrees_(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        Approach: Rotate four rectangles in one single loop.
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        :param matrix:
        :return:
        """
        n = len(matrix[0])
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                temp = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
                matrix[j][n - 1 - i] = matrix[i][j]
                matrix[i][j] = temp
        return matrix


if __name__ == "__main__":
    rotate_image = RotateImage()
    print(rotate_image.to_90_degrees(
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
    ))
    print(rotate_image.to_90_degrees_(
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
    ))
