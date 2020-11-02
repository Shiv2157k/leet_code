from typing import List


class Zeros:

    def mark_(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        Approach: Using set
        Time Complexity: O(MN)
        Space Complexity: O(MN)
        :param matrix:
        :return:
        """
        rows, cols = len(matrix), len(matrix[0])
        row_set, col_set = set(), set()

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    row_set.add(row)
                    col_set.add(col)

        for row in range(rows):
            for col in range(cols):
                if row in row_set or col in col_set:
                    matrix[row][col] = 0
        return matrix

    def mark(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        Approach: Without extra space
        Time Complexity: O(MN)
        Space Complexity: O(1)
        :param matrix:
        :return:
        """
        rows, cols = len(matrix), len(matrix[0])
        is_col = False

        # mark all the diagonals/ adjacent to zero
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

        # mark all the first row to zero
        if matrix[row][col] == 0:
            for col in range(cols):
                matrix[0][col] = 0

        # mark all the firs col to zero
        if is_col:
            for row in range(rows):
                matrix[row][0] = 0

        return matrix


if __name__ == "__main__":
    zeros = Zeros()
    print(zeros.mark_(
        [
            [0, 1, 2, 0],
            [3, 4, 5, 2],
            [1, 3, 1, 5]
        ]
    ))
    print(zeros.mark(
        [
            [0, 1, 2, 0],
            [3, 4, 5, 2],
            [1, 3, 1, 5]
        ]
    ))
    print(zeros.mark_(
        [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ]
    ))
    print(zeros.mark(
        [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ]
    ))