from typing import List


class Triangle:

    def get_minimum_sum(self, triangle: List[List[int]]) -> int:
        """
        Approach: Bottom up
        :param triangle:
        :return:
        """
        if not triangle:
            return

        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
        return triangle[0][0]

    def get_minimum_sum_(self, triangle: List[List[int]]) -> int:
        """
        Approach: Bottom up with O(n) space.
        :param triangle:
        :return:
        """
        if not triangle:
            return

        path = triangle[-1]
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                path[j] = min(path[j], path[j + 1]) + triangle[i][j]
        return path[0]


if __name__ == "__main__":

    triangle_ = Triangle()
    print(triangle_.get_minimum_sum(
        [
            [-1],
            [2, 3],
            [1, -1, -3]
        ]
    ))
    print(triangle_.get_minimum_sum_(
        [
            [-1],
            [2, 3],
            [1, -1, -3]
        ]
    ))