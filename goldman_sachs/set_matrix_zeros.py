from typing import List
from pprint import pprint


class ZeroMatrix:

    def set_(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        Approach: Using Set
        Time Complexity: O(MN)
        Space Complexity: O(N)
        :param matrix:
        :return:
        """

        rows, cols = len(matrix), len(matrix[0])
        col_set, row_set = set(), set()

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    col_set.add(col)
                    row_set.add(row)

        for row in range(rows):
            for col in range(cols):
                if row in row_set or col in col_set:
                    matrix[row][col] = 0
        return matrix

    def set_with_constant_space(self, matrix: List[List[int]]) -> List[int]:
        """
        Approach: Constant Space
        Time Complexity: O(MN)
        Space Complexity: O(1)
        :param matrix:
        :return:
        """

        rows, cols = len(matrix), len(matrix[0])

        is_col = False

        for row in range(rows):
            if matrix[row][0] == 0:
                is_col = True
            for col in range(1, cols):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        for row in range(1, rows):
            for col in range(1, cols):
                if not matrix[row][0] or not matrix[0][col]:
                    matrix[row][col] = 0

        if matrix[0][0] == 0:
            for col in range(cols):
                matrix[0][col] = 0

        if is_col:
            for row in range(rows):
                matrix[row][0] = 0
        return matrix


if __name__ == "__main__":
    m = ZeroMatrix()
    pprint(m.set_(
        [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ]
    ))
    pprint(m.set_with_constant_space(
        [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ]
    ))
    pprint(m.set_(
        [
            [0, 1, 2, 0],
            [3, 4, 5, 2],
            [1, 3, 1, 5]
        ]
    ))
    pprint(m.set_with_constant_space(
        [
            [0, 1, 2, 0],
            [3, 4, 5, 2],
            [1, 3, 1, 5]
        ]
    ))

