from typing import List


class RainWater:

    def total_area_trapped(self, heights: List[int]) -> int:
        """
        Approach: Two Pointers Optimized
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param heights:
        :return:
        """

        if not heights:
            return 0

        left_max = right_max = 0
        left, right = 0, len(heights) - 1
        water_area = 0

        while left < right:

            if heights[left] < heights[right]:
                left_max = max(left_max, heights[left])
                water_area += left_max - heights[left]
                left += 1
            else:  # heights[left] >= heights[right]
                right_max = max(right_max, heights[right])
                water_area += right_max - heights[right]
                right -= 1
        return water_area

    def total_area_trapped_(self, heights: List[int]) -> int:
        """
        Approach: Two Pointers
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param height:
        :return:
        """

        if not heights:
            return 0

        water_area = 0
        left_max = [0] * len(heights)
        right_max = [0] * len(heights)

        left_max[0], right_max[-1] = heights[0], heights[-1]

        for i in range(1, len(heights)):
            left_max[i] = max(heights[i], left_max[i - 1])
        for i in range(len(heights) - 2, -1, -1):
            right_max[i] = max(heights[i], right_max[i + 1])
        for i in range(1, len(heights)):
            water_area += min(left_max[i], right_max[i]) - heights[i]
        return water_area


if __name__ == "__main__":
    rain_water = RainWater()
    print(rain_water.total_area_trapped([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(rain_water.total_area_trapped_([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
