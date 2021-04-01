from typing import List


class WaterContainer:

    def with_most_water(self, height: List[int]) -> int:
        """
        Approach: Two Pointers
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param height:
        :return:
        """
        left, right = 0, len(height) - 1
        area = 0
        while left < right:

            area = max(area, min(height[left], height[right]) * (right - left))

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return area


if __name__ == "__main__":
    container = WaterContainer()
    print(container.with_most_water([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(container.with_most_water([1, 1, 1, 1, 1, 1, 1, 1, 1]))