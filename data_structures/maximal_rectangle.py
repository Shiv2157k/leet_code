from typing import List


class Matrix:

    def histogram_area(self, heights: List[int]) -> int:
        """
        Gets the histogram area.
        :param heights:
        :return:
        """
        max_area, stack = 0, [-1]

        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                max_area = max(max_area, heights[stack.pop()] * (i - stack[-1] - 1))
            stack.append(i)

        while stack[-1] != -1:
            max_area = max(max_area, heights[stack.pop()] * (len(heights) - stack[-1] - 1))
        return max_area

    def get_max_rectangle_area(self, matrix: List[str]) -> int:
        """
        Approach: Histogram - Stack
        Time Complexity: O(MN)
        Space Complexity: O(N)
        :param matrix:
        :return:
        """
        # base case
        if not matrix:
            return 0

        m, n, max_area = len(matrix), len(matrix[0]), 0
        dp = [0] * n

        for i in range(m):
            for j in range(n):
                dp[j] = dp[j] + 1 if matrix[i][j] == "1" else 0

            max_area = max(max_area, self.histogram_area(dp))
        return max_area

    def get_max_rectangle_area_(self, matrix: List[str]) -> int:
        """
        Approach: DP - Max height at each point.
        Time Complexity: O(NM)
        Space Complexity: O(N)
        :param matrix:
        :return:
        """
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        left, height, right, max_area = [0] * n, [0] * n, [n] * n, 0
        for i in range(m):
            curr_left, curr_right = 0, n

            # update height
            for j in range(n):
                if matrix[i][j] == "1":
                    height[j] += 1
                else:
                    height[j] = 0
            # update left
            for j in range(n):
                if matrix[i][j] == "1":
                    left[j] = max(left[j], curr_left)
                else:
                    left[j], curr_left = 0, j + 1
            # update right
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == "1":
                    right[j] = min(right[j], curr_right)
                else:
                    right[j], curr_right = n, j

            # update max_area
            for j in range(n):
                max_area = max(max_area, height[j] * (right[j] - left[j]))
        return max_area


if __name__ == "__main__":
    rectangle = Matrix()
    print(rectangle.get_max_rectangle_area([
        ["1", "0", "1", "1", "1"],
        ["1", "0", "1", "0", "0"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]))
    print(rectangle.get_max_rectangle_area_([
        ["1", "0", "1", "1", "1"],
        ["1", "0", "1", "0", "0"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]))
    print(rectangle.get_max_rectangle_area([
        ["1", "0", "0", "1", "1", "1"],
        ["1", "0", "1", "1", "0", "1"],
        ["0", "1", "1", "1", "1", "1"],
        ["0", "0", "1", "1", "1", "1"]
    ]))
    print(rectangle.get_max_rectangle_area_([
        ["1", "0", "0", "1", "1", "1"],
        ["1", "0", "1", "1", "0", "1"],
        ["0", "1", "1", "1", "1", "1"],
        ["0", "0", "1", "1", "1", "1"]
    ]))
