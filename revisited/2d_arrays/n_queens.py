from typing import List
from pprint import pprint


class Queens:

    def get_all_distinct_solutions(self, n: int) -> int:
        """
        Approach: Back tracking
        Time Complexity: O(N!)
        Space Complexity: O(N)
        :param n:
        :return:
        """
        def could_place(row: int, col: int) -> bool:
            return not (cols[col] + hills[row + col] + dales[row - col])

        def place_queen(row: int, col: int):
            cols[col] = 1
            hills[row + col] = 1
            dales[row - col] = 1

        def remove_queen(row: int, col: int):
            cols[col] = 0
            hills[row + col] = 0
            dales[row - col] = 0

        def back_track(row: int = 0, count: int = 0):
            for col in range(n):
                if could_place(row, col):
                    place_queen(row, col)
                    if row + 1 == n:
                        count += 1
                    else:
                        count = back_track(row + 1, count)
                    remove_queen(row, col)
            return count

        cols = [0] * n
        hills = [0] * (2 * n - 1)
        dales = [0] * (2 * n - 1)
        return back_track()

    def place_n_(self, n: int) -> List[List[str]]:
        """
        Approach: Back Tracking
        Time Complexity: O(N!)
        Space Complexity: O(N)
        :param n:
        :return:
        """

        def could_place(row: int, col: int) -> bool:
            """
            Determines if we can place the queen on the cell or not.
            :param row:
            :param col:
            :return:
            """
            return not (cols[col] + hills[row + col] + dales[row - col])

        def place_queen(row: int, col: int):
            """
            Places the queen on the cell.
            :param row:
            :param col:
            :return:
            """
            queens.add((row, col))
            cols[col] = 1
            hills[row + col] = 1
            dales[row - col] = 1

        def remove_queen(row: int, col: int):
            """
            Removes the queen from the cell.
            :param row:
            :param col:
            :return:
            """
            queens.remove((row, col))
            cols[col] = 0
            hills[row + col] = 0
            dales[row - col] = 0

        def add_solution():
            """
            Adds the solution on to the output
            :return:
            """
            solution = []
            for _, col in sorted(queens):
                solution.append("." * col + "Q" + "." * (n - col - 1))
            output.append(solution)

        def back_track(row=0):
            """
            Back tracks from the dead end and moves to the
            possible solution.
            :param row:
            :return:
            """
            for col in range(n):
                if could_place(row, col):
                    place_queen(row, col)
                    if row + 1 == n:
                        add_solution()
                    else:
                        back_track(row + 1)
                    remove_queen(row, col)

        cols = [0] * n
        hills = [0] * (2 * n - 1)
        dales = [0] * (2 * n - 1)

        queens = set()
        output = []
        back_track()
        return output

    def place_n(self, n: int) -> List[List[str]]:
        """
        Approach: Increasing the row tracker.
        :param n:
        :return:
        """

        def place_queens(row: int, n: int, queens: List[int]) -> List[int]:
            """
            Places the queens on the right columns in a row.
            :param row:
            :param n:
            :param queens:
            :return:
            """
            # if row reached n then found solution
            if row == n:
                return [queens]
            result = []
            for col in range(n):
                if could_place(row, col, queens):
                    result += place_queens(row + 1, n, queens + [col])
            return result

        def could_place(row: int, col: int, queens: List[int]) -> bool:
            """
            Checks if a queen can be placed in that row or not.
            :param row:
            :param col:
            :param queens:
            :return:
            """
            for r, c in enumerate(queens):
                # checks if queen is placed on same column
                # and same diagonal
                # if it is then return False
                if c == col or abs(row - r) == abs(col - c):
                    return False
            return True

        result = place_queens(0, n, [])
        return [["".join(["Q" if c == col else "." for c in range(n)]) for col in queens] for queens in result]


if __name__ == "__main__":
    n_queens = Queens()
    pprint(n_queens.place_n(4))
    pprint(n_queens.place_n_(4))
    print(n_queens.get_all_distinct_solutions(4))