from typing import List


class RainWater:

    def trap_(self, heights: List[int]) -> int:
        """
        Approach: Two Pointers
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param heights:
        :return:
        """

        if not heights:
            return 0

        area, size = 0, len(heights)
        left_max = [0 for _ in range(size)]
        right_max = [0 for _ in range(size)]

        left_max[0], right_max[-1] = heights[0], heights[-1]

        for i in range(1, size):
            left_max[i] = max(heights[i], left_max[i - 1])
        for i in range(size - 2, -1, -1):
            right_max[i] = max(heights[i], right_max[i + 1])
        for i in range(1, size):
            area += min(left_max[i], right_max[i]) - heights[i]
        return area

    def trap(self, heights: List[int]) -> int:
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
            if heights[left] < heights[right]:  # move left
                left_max = max(left_max, heights[left])
                water_area += left_max - heights[left]
                left += 1
            else:  # move right
                right_max = max(right_max, heights[right])
                water_area += right_max - heights[right]
                right -= 1
        return water_area

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

    print(rain_water.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(rain_water.trap([4, 2, 0, 3, 2, 5]))

    print(rain_water.trap_([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(rain_water.trap_([4, 2, 0, 3, 2, 5]))

