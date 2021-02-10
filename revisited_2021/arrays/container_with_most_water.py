from typing import List


class Container:

    def get_max_container_area(self, height: List[int]) -> int:
        """
        Approach: Two Pointers (Single Pass)
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param height:
        :return:
        """
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            max_area = max(max_area, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area


if __name__ == "__main__":
    container = Container()
    print(container.get_max_container_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
