from typing import List


class TrappingRainWater:

    def get_area(self, height: List[int]) -> int:
        """
        Approach: Two Pointer
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param height:
        :return:
        """
        left, right = 0, len(height) - 1
        left_max = right_max = water_area = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                water_area += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                water_area += right_max - height[right]
                right -= 1
        return water_area


if __name__ == "__main__":
    trapped_rain_water = TrappingRainWater()
    print(trapped_rain_water.get_area([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))