from typing import List


class Histogram:

    def find_largest_rectangle_area(self, heights: List[int]) -> int:
        """
        Approach: Using Stack
        Time complexity :O(N)
        Space Complexity: O(N)
        :param heights:
        :return:
        """
        stack, max_area = [-1], 0
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                max_area = max(max_area, heights[stack.pop()] * (i - stack[-1] - 1))
            stack.append(i)

        while stack[-1] != -1:
            max_area = max(max_area, heights[stack.pop()] * (len(heights) - stack[-1] - 1))
        return max_area


if __name__ == "__main__":
    histogram = Histogram()
    print(histogram.find_largest_rectangle_area([2, 1, 5, 6, 2, 3]))
    print(histogram.find_largest_rectangle_area([6, 7, 5, 2, 4, 5, 9, 3]))