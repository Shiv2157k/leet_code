from typing import List


class Triangle:

    def get_minimum_path_sum(self, triangle: List[List[int]]) -> int:
        """
        Approach: DP
        Time Complexity: O(N^2)
        Space Complexity: O(N)
        :param triangle:
        :return:
        """
        # base case
        if not triangle:
            return

        result = triangle[-1]
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                result[j] = min(result[j], result[j + 1]) + triangle[i][j]
        return result[0]


if __name__ == "__main__":
    tri = Triangle()
    print(tri.get_minimum_path_sum(
        [
            [2],
            [3, 4],
            [6, 5, 7],
            [4, 1, 8, 3]
        ]))