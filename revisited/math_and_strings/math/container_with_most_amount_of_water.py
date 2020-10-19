from typing import List


class Container:

    def get_max_area(self, heights: List[int]) -> int:
        """
        Approach: One Pass
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param heights:
        :return:
        """
        max_area = left = 0
        right = len(heights) - 1
        while left < right:
            max_area = max(max_area, min(heights[left], heights[right]) * (right - left))
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_area

    def get_max_area_(self, heights: List[int]) -> int:
        """
        Approach: Brute Force
        Time Complexity: O(N^2)
        Space Complexity: O(1)
        :param heights:
        :return:
        """
        max_area = 0

        for left in range(len(heights)):
            for right in range(1, len(heights)):
                max_area = max(max_area, min(heights[left], heights[right]) * (right - left))
        return max_area


if __name__ == "__main__":
    container = Container()
    print(container.get_max_area_([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(container.get_max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(container.get_max_area_([1, 1]))
    print(container.get_max_area([1, 1]))
    print(container.get_max_area_([1, 8]))
    print(container.get_max_area([1, 8]))
    print(container.get_max_area_([1, 8, 4]))
    print(container.get_max_area([1, 8, 4]))
