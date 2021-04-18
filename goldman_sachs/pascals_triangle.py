from typing import List
from pprint import pprint


class PascalTriangle:

    def build(self, num_rows: int) -> List[List[int]]:

        if not num_rows:
            return []

        triangle = []

        for row_num in range(num_rows):
            row = [None for _ in range(row_num + 1)]
            row[0], row[-1] = 1, 1
            for internal in range(1, len(row) - 1):
                row[internal] = triangle[row_num - 1][internal - 1] + triangle[row_num - 1][internal]
            triangle.append(row)
        return triangle


if __name__ == "__main__":
    pascal_triangle = PascalTriangle()
    pprint(pascal_triangle.build(5))