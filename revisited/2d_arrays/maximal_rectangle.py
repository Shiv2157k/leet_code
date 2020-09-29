from typing import List


class Rectangle:

    def get_maximum_area(self, matrix: List[List[str]]) -> int:
        """
        Approach: Maximum Area at each point.
        Time Complexity: O(MN)
        Space Complexity: O(N)
        :param matrix:
        :return:
        """
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        left = [0] * n
        right = [n] * n
        height = [0] * n
        max_area = 0

        for i in range(m):
            curr_left, curr_right = 0, n

            # update height
            for j in range(n):
                height[j] = height[j] + 1 if matrix[i][j] == "1" else 0

            # update left
            for j in range(n):
                if matrix[i][j] == "1":
                    left[j] = max(left[j], curr_left)
                else:
                    left[j] = 0
                    curr_left = j + 1

            # update right
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == "1":
                    right[j] = min(right[j], curr_right)
                else:
                    right[j] = n
                    curr_right = j

            # calculate max area
            for j in range(n):
                max_area = max(max_area, height[j] * (right[j] - left[j]))
        return max_area

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
    print(rectangle.get_maximum_area(
        [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"]
        ]
    ))
    print(rectangle.get_maximal_with_1(
        [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"]
        ]
    ))