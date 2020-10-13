from typing import List
from pprint import pprint


class PascalTriangle:

    def get_nth_row(self, num_rows: int) -> List[List[int]]:
        """
        Approach: DP
        Time Complexity: O(num_rows^2)
        Space Complexity: O(num_row)
        :param num_rows:
        :return:
        """
        if not num_rows:
            return []

        pascal = [1] * (num_rows + 1)
        for i in range(2, num_rows + 1):
            for j in range(1, i):
                pascal[i - j] += pascal[i - j - 1]
        return pascal

    def generate(self, num_rows: int) -> List[List[int]]:
        """
        Approach: DP
        Time Complexity: O(num_rows^2)
        Space Complexity: O(num_rows^2)
        :param num_rows:
        :return:
        """
        if not num_rows:
            return []
        triangle = []

        # first outer loop
        for row_num in range(num_rows):
            row = [None for _ in range(row_num + 1)]
            # mark the first and last index as 1
            row[0], row[-1] = 1, 1
            # loop from index 1  to last index - 1
            for j in range(1, len(row) - 1):
                row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]
            # append rows to triangle after generating.
            triangle.append(row)
        return triangle


if __name__ == "__main__":
    pascal_triangle = PascalTriangle()
    pprint(pascal_triangle.generate(5))
    pprint(pascal_triangle.get_nth_row(4))
