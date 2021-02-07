from typing import List
from pprint import pprint


class Pascal:

    def generate_triangle(self, num_rows: int) -> List[List[int]]:
        """
        Approach: DP
        Time Complexity: O(N^2)
        Space Complexity: O(N^2)
        :param num_rows:
        :return:
        """
        if not num_rows:
            return [[]]
        triangle = []
        for row_num in range(num_rows):
            row = [None for _ in range(row_num + 1)]
            row[0], row[-1] = 1, 1
            for i in range(1, len(row) - 1):
                row[i] = triangle[row_num - 1][i - 1] + triangle[row_num - 1][i]
            triangle.append(row)
        return triangle

    def generate(self, num_rows: int) -> List[List[int]]:
        """
        Approach:
        Time Complexity: O(N^2)
        Space Complexity: O(N^2)
        :param num_rows:
        :return:
        """
        if num_rows == 0:
            return [[]]
        triangle = [[1]]
        for num in range(1, num_rows):
            triangle += [list(map(lambda x, y: x + y, [0] + triangle[-1], triangle[-1] + [0]))]
        return triangle


if __name__ == "__main__":
    pascal = Pascal()
    pprint(pascal.generate_triangle(5))
    pprint(pascal.generate(5))

