from typing import List


class Triangle:

    def get_min_path_sum(self, triangle: List[List[int]]) -> int:
        """
        Approach: DP
        Time Complexity: O(N^2)
        Space Complexity: O(N)
        :param triangle:
        :return:
        """
        if not triangle:
            return

        dp = triangle[-1]

        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                dp[col] = min(dp[col], dp[col + 1]) + triangle[row][col]
        return dp[0]


if __name__ == "__main__":
    triangle = Triangle()
    print(triangle.get_min_path_sum(
        [
            [2],
            [3, 4],
            [6, 5, 7],
            [4, 1, 8, 3]
        ]
    ))