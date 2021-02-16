from typing import List


class Array:

    def rotate_(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        Approach: Transpose and Reverse
        Time Complexity: O(M)
        Space Complexity: O(1)
        :param matrix:
        :return:
        """
        matrix = self.transpose(matrix)
        return self.reverse(matrix)

    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix[0])
        for r in range(n):
            for c in range(r, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        return matrix

    def reverse(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix[0])
        for r in range(n):
            for c in range(n // 2):
                matrix[r][c], matrix[r][-c - 1] = matrix[r][-c-1], matrix[r][c]
        return matrix

    def rotate__(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        Approach: Transpose and in-built reverse
        Time Complexity: O(M)
        Space Complexity: O(1)
        :param matrix:
        :return:
        """
        rows = len(matrix)
        cols = len(matrix[0])

        for r in range(rows):
            for c in range(r, cols):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        for r in range(rows):
            matrix[r].reverse()
        return matrix

    def rotate(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        Approach: Rotate Groups of Four cells
        Time Complexity: O(M)
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


if __name__ == "__main__":
    array = Array()
    print(array.rotate__([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(array.rotate_([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(array.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
