from typing import List


class Container:

    def with_most_water(self, heights: List[int]) -> int:
        """
        Approach: Two Pointer
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param heights:
        :return:
        """

        if not heights:
            return 0

        left, right = 0, len(heights) - 1
        max_area = 0

        while left <= right:

            max_area = max(max_area, min(heights[left], heights[right]) * (right - left))
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_area


if __name__ == "__main__":
    container = Container()
    print(container.with_most_water([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(container.with_most_water([1, 1]))
    print(container.with_most_water([4, 3, 2, 1, 4]))
    print(container.with_most_water([1, 2, 1]))
