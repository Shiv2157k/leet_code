from typing import List


class Rectangle:

    def histogram(self, heights: List[int]):
        """
        Approach: Using Stack
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param heights:
        :return:
        """
        stack, max_area, size = [-1], 0, len(heights)
        for i in range(size):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                max_area = max(max_area, heights[stack.pop()] * (i - stack[-1] - 1))
            stack.append(i)
        while stack[-1] != -1:
            max_area = max(max_area, heights[stack.pop()] * (size - stack[-1] - 1))
        return max_area

    def get_maximal_with_1(self, matrix: List[List[str]]) -> int:
        """
        Approach: DP with histogram
        Time Complexity: O(MN)
        Space Complexity: O(N)
        :param matrix:
        :return:
        """
        if not matrix:
            return 0

        dp = [0] * len(matrix[0])
        max_area = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dp[j] = dp[j] + 1 if matrix[i][j] == "1" else 0
            max_area = max(max_area, self.histogram(dp))
        return max_area


if __name__ == "__main__":
    rectangle = Rectangle()
    print(rectangle.get_maximal_with_1(
        [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"]
        ]
    ))