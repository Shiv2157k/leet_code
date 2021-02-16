from typing import List


class Matrix:

    def spiral_order(self, matrix: List[List[int]]) -> List[int]:
        """
        Approach: Simulation
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param matrix:
        :return:
        """
        rows, cols = len(matrix), len(matrix[0])
        seen = [[False] * cols for _ in range(rows)]
        dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]
        row = col = di = 0
        spiral = []
        for _ in range(rows * cols):
            spiral.append(matrix[row][col])
            seen[row][col] = True
            cr, cc = row + dr[di], col + dc[di]
            if 0 <= cr < rows and 0 <= cc < cols and not seen[cr][cc]:
                row, col = cr, cc
            else:
                di = (di + 1) % 4
                row, col = row + dr[di], col + dc[di]
        return spiral


if __name__ == "__main__":
    array = Matrix()
    print(array.spiral_order(
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
    ))
