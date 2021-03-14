from typing import List


class RainWater:

    def trapped(self, heights: List[int]) -> int:
        """
        Approach: Two Pointers
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param heights:
        :return:
        """
        left, right = 0, len(heights) - 1
        left_max = right_max = water_area = 0

        while left < right:
            if heights[left] < heights[right]:
                if heights[left] > left_max:
                    left_max = heights[left]
                water_area += left_max - heights[left]
                left += 1
            else:
                if heights[right] > right_max:
                    right_max = heights[right]
                water_area += right_max - heights[right]
                right -= 1
        return water_area


if __name__ == "__main__":
    rain_water = RainWater()
    print(rain_water.trapped([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(rain_water.trapped([4, 2, 0, 3, 2, 5]))
