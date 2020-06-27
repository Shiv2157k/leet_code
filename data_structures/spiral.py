from typing import List


class Spiral:

    def get_order(self, matrix: List[List[int]]) -> List[int]:
        """
        Approach: Simulation
        Time Complexity: O(n)
        Space Complexity: O(n)
        :param matrix:
        :return:
        """
        # validation
        if not matrix:
            return []

        order, rows, cols = [], len(matrix), len(matrix[0])
        seen = [[False] * cols for _ in range(rows)]
        row_directions, col_directions = [0, 1, 0, -1], [1, 0, -1, 0]
        row = col = di = 0

        for _ in range(rows * cols):
            order.append(matrix[row][col])
            seen[row][col] = True
            cr, cc = row + row_directions[di], col + col_directions[di]
            if 0 <= cr < rows and 0 <= cc < cols and not seen[cr][cc]:
                row, col = cr, cc
            else:
                di = (di + 1) % 4
                row, col = row + row_directions[di], col + col_directions[di]
        return order


if __name__ == "__main__":
    spiral = Spiral()
    print(spiral.get_order(
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
    ))
