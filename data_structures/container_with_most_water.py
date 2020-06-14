from typing import List


class Container:

    def get_max_area(self, height: List) -> int:
        """
        Approach: Two Pointers Approach.
        Time Complexity: O(n)
        Space Complexity: O(n)
        :param height:
        :return:
        """

        left, right, max_area = 0, len(height) - 1, 0

        while left < right:

            max_area = max(max_area, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area


if __name__ == "__main__":
    container = Container()
    print(container.get_max_area([1, 7, 8, 4, 5, 8, 7, 5]))