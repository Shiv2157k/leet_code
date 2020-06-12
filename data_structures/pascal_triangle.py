from typing import List


class Triangle:

    def build_pascal_(self, num_rows: int) -> List[List[int]]:
        """
        Approach: Using map and lambda functions.
        :param num_rows:
        :return:
        """
        if num_rows == 0:
            return []

        res = [[1]]
        for _ in range(1, num_rows):
            # for _ = 1 : [0, 1] + [1, 0] = [1, 1] ...
            res += [list(map(lambda i, j: i + j, [0] + res[-1], res[-1] + [0]))]
        return res

    def build_pascal(self, num_rows: int) -> List[List[int]]:
        """
        Approach: DP
        Time Complexity: O(num_rows ^ 2)
        Space Complexity: O(num_rows ^ 2)
        :param num_rows:
        :return:
        """
        tri_angle = []

        for num_row in range(num_rows):

            row = [None for _ in range(num_row + 1)]
            row[0] = row[-1] = 1

            for j in range(1, num_row):
                row[j] = tri_angle[num_row - 1][j - 1] + tri_angle[num_row - 1][j]

            tri_angle.append(row)
        return tri_angle

    def get_row(self, num_rows: int) -> List[int]:

        pascal = [1] * (num_rows + 1)
        for i in range(2, num_rows + 1):
            for j in range(1, i):
                pascal[i - j] += pascal[i - j - 1]
        return pascal


if __name__ == "__main__":
    triangle = Triangle()
    print(triangle.build_pascal(6))
    print(triangle.build_pascal_(6))
    print(triangle.get_row(5))
