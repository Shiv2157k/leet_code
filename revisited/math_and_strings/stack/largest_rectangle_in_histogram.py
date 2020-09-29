from typing import List


class Histogram:

    def get_max_rectangle_area(self, heights: List[int]) -> int:
        """
        Approach: Stack
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

    def get_max_area_rectangle(self, heights: List[int]) -> int:
        """
        Approach: Brute Force
        Time Complexity: O(N^2)
        Space Complexity: O(N)
        :param heights:
        :return:
        """

        max_area = 0

        for i in range(len(heights)):
            min_height = float("inf")
            for j in range(i, len(heights)):
                min_height = min(min_height, heights[j])
                max_area = max(max_area, min_height * (j - i + 1))
        return max_area


if __name__ == "__main__":
    histogram = Histogram()
    print(histogram.get_max_area_rectangle([6, 7, 5, 2, 4, 5, 9, 3]))
    print(histogram.get_max_rectangle_area([6, 7, 5, 2, 4, 5, 9, 3]))