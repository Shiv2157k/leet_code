from typing import List


class Matrix:

    def gen_spiral(self, matrix: List[List[int]]) -> List[int]:
        """
        Approach: Clock-wise
        Time Complexity : O(N)
        Space Complexity: O(1) if ignored the spiral storage else O(N)
        :param matrix:
        :return:
        """
        def spiral_coordinates(r1: int, c1: int, r2: int, c2: int):
            # move right
            for c in range(c1, c2 + 1):
                yield r1, c
            # move down
            for r in range(r1 + 1, r2 + 1):
                yield r, c2
            if r1 < r2 and c1 < c2:
                # move up
                for c in range(c2 - 1, c1, -1):
                    yield r2, c
                # move left
                for r in range(r2, r1, -1):
                    yield r, c1

        # base case
        if not matrix:
            return []

        r1, r2 = 0, len(matrix) - 1
        c1, c2 = 0, len(matrix[0]) - 1
        spiral = []

        while r1 <= r2 and c1 <= c2:
            for r, c in spiral_coordinates(r1, c1, r2, c2):
                spiral.append(matrix[r][c])
            r1 += 1
            r2 -= 1
            c1 += 1
            c2 -= 1
        return spiral


    def generate_spiral(self, matrix: List[List[int]]) -> List[int]:
        """
        Approach: Simulation
        N -> Total number of elements in the input matrix.
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param matrix:
        :return:
        """
        if not matrix:
            return []
        rows, cols = len(matrix), len(matrix[0])
        # too keep track of visited cells
        seen = [[False] * cols for _ in range(rows)]
        # to move the directions right -> down -> left -> up ..
        dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]
        # to iterate over each cell
        row = col = di = 0
        # to save the spiral pattern
        spiral = []

        for _ in range(rows * cols):
            spiral.append(matrix[row][col])
            # marking the visited row
            seen[row][col] = True
            # calculating next cell indexes
            cr, cc = row + dr[di], col + dc[di]
            # checking the boundary conditions
            if 0 <= cr < rows and 0 <= cc < cols and not seen[cr][cc]:
                row, col = cr, cc
            else: # changing the direction
                di = (di + 1) % 4
                row, col = row + dr[di], col + dc[di]
        return spiral


if __name__ == "__main__":
    spiral_matrix = Matrix()
    print(spiral_matrix.generate_spiral(
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
    ))
    print(spiral_matrix.generate_spiral(
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]
        ]
    ))
    print(spiral_matrix.gen_spiral(
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
    ))
    print(spiral_matrix.gen_spiral(
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]
        ]
    ))
