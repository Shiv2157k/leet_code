from typing import List


class RainWater:

    def get_area(self, height: List[int]) -> int:
        """
        Approach: Two Pointers
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param height:
        :return:
        """
        left, right = 0, len(height) - 1
        left_max = right_max = water_area = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] > left_max:
                    left_max = height[left]
                water_area += left_max - height[left]
                left += 1
            else:
                if height[right] > right_max:
                    right_max = height[right]
                water_area += right_max - height[right]
                right -= 1
        return water_area

    def get_area_(self, height: List[int]) -> int:
        """
        Approach: Pointers
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param height:
        :return:
        """
        size = len(height)
        left = [0] * size
        right = [0] * size
        left[0], right[-1] = height[0], height[-1]
        area = 0
        for i in range(1, size):
            left[i] = max(left[i - 1], height[i])
        for i in range(size - 2, -1, -1):
            right[i] = max(right[i + 1], height[i])
        for i in range(size):
            area += min(left[i], right[i]) - height[i]
        return area


if __name__ == "__main__":
    rain_water = RainWater()
    print(rain_water.get_area([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(rain_water.get_area_([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
