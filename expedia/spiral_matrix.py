from typing import List


class SpiralMatrix:

    def generate(self, matrix: List[List[int]]) -> List[int]:
        """
        Approach: Simulation
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param matrix:
        :return:
        """

        rows, cols = len(matrix), len(matrix[0])

        dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]

        seen = [[False] * cols for _ in range(rows)]

        row = col = di = 0
        spiral = []

        for _ in range(rows * cols):

            spiral.append(matrix[row][col])
            seen[row][col] = True

            cr = row + dr[di]
            cc = col + dc[di]

            if 0 <= cr < rows and 0 <= cc < cols and not seen[cr][cc]:
                row, col = cr, cc
            else:
                di = (di + 1) % 4
                row, col = row + dr[di], col + dc[di]
        return spiral


if __name__ == "__main__":

    spiral_matrix = SpiralMatrix()
    print(spiral_matrix.generate(
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
    ))
    print(spiral_matrix.generate(
        [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20]
        ]
    ))


