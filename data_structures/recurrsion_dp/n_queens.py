from typing import List


class Queens:

    def solve_position(self, n: int) -> List[List[str]]:
        """
        Approach: Back tracking
        Time Complexity: O(N!)
        Space Complexity: O(N)
        :param n:
        :return:
        """

        def could_place(row: int, col: int) -> bool:
            """
            Verifies if the queen can be placed or not.
            :param row:
            :param col:
            :return:
            """
            return not (cols[col] + hill_diagonals[row - col] + dale_diagonals[row + col])

        def place_queen(row: int, col: int):
            """
            Places the queen into the grid.
            :param row:
            :param col:
            :return:
            """
            queens.add((row, col))
            cols[col] = 1
            hill_diagonals[row - col] = 1
            dale_diagonals[row + col] = 1

        def remove_queen(row: int, col: int):
            """
            Removes the queen into the grid.
            :param row:
            :param col:
            :return:
            """
            queens.remove((row, col))
            cols[col] = 0
            hill_diagonals[row - col] = 0
            dale_diagonals[row + col] = 0

        def add_position():
            """
            Adds the queen into their right positions.
            :return:
            """
            solution = []
            for _, col in sorted(queens):
                solution.append("." * col + "Q" + "." * (n - col - 1))
            output.append(solution)

        def back_track(row=0):
            for col in range(n):
                if could_place(row, col):
                    place_queen(row, col)
                    if row + 1 == n:
                        add_position()
                    else:
                        back_track(row + 1)
                    remove_queen(row, col)

        cols = [0] * n
        hill_diagonals = [0] * (2 * n - 1)
        dale_diagonals = [0] * (2 * n - 1)

        queens = set()
        output = []
        back_track()
        return output


if __name__ == "__main__":
    queens = Queens()
    print(queens.solve_position(5))
    print(queens.solve_position(4))
    print(queens.solve_position(3))