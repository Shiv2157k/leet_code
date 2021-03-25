from typing import List


class TrappingRainWater:

    def get_area(self, height: List[int]):
        """
        Approach: Two Pointers
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param height:
        :return:
        """

        left, right = 0, len(height) - 1
        left_area = right_area = water_area = 0

        while left < right:
            if height[left] < height[right]:
                left_area = max(left_area, height[left])
                water_area += left_area - height[left]
                left += 1
            else:
                right_area = max(right_area, height[right])
                water_area += right_area - height[right]
                right -= 1
        return water_area


if __name__ == "__main__":
    rain_water = TrappingRainWater()
    print(rain_water.get_area(
        [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    ))