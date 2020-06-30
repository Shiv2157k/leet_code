from typing import List


class Matrix:

    def set_to_zeros(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        Approach: O(1) Space, Iteration.
        Time Complexity: O(M * N)
        Space Complexity: O(1)
        :param matrix:
        :return:
        """
        # get the number of rows and columns
        columns, rows = len(matrix), len(matrix[0])
        # bool to check if any column has zero
        is_column = False

        # iterate to set all the adjacent elements to zero if the
        # [i][j] = 0 and set is_col to true if we encounter any
        # column is 0
        for col in range(columns):
            if matrix[col][0] == 0:
                is_column = True
            for row in range(1, rows):
                if matrix[col][row] == 0:
                    matrix[col][0] = 0
                    matrix[0][row] = 0

        # re-iterate over the matrix to set elements to zero
        # based on the first row and column
        for col in range(1, columns):
            for row in range(1, rows):
                if not matrix[col][0] or not matrix[0][row]:
                    matrix[col][row] = 0

        # set all the first rows to zeroes
        if matrix[0][0] == 0:
            for row in range(rows):
                matrix[0][row] = 0

        # set all the first columns to zeroes
        if is_column:
            for col in range(columns):
                matrix[col][0] = 0
        return matrix


if __name__ == "__main__":
    matrix_board = Matrix()
    print(matrix_board.set_to_zeros(
        [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ]
    ))
    print(matrix_board.set_to_zeros(
        [
            [0, 1, 2, 0],
            [3, 4, 5, 2],
            [1, 3, 1, 5]
        ]
    ))