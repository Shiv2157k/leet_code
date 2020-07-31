from typing import List


class ElevationMap:
    """
    Formulae to find trapping rain water:
    elevation = [0, 2, 3]
                [0, 1, 2]
    current_index = 1
    water_area = minimum(
                            maximum(elevation[previous], elevation[current]),
                            maximum(elevation[current], elevation[next])
                        ) -
                        elevation[current]
    """

    def get_trapped_rain_water_area(self, height:List[int]) -> int:
        """
        Approach: Two Pointers
        Time Complexity: O(n)
        Space Complexity: O(1)
        Algorithm:
            - Initialize left and right pointer with 0 and last elevation position
            - loop until left is less than right
            - if elevation of left positioned is less then elevation of right positioned
                - if left elevation is greater than max left elevation
                    - update the max left elevation
                - calculate the area: area += left max elevation - elevation of current left position
                - increment the left elevation position by 1
            - else if the left elevation is greater then the right elevation
                - if right elevation is greater than or equal to right max elevation
                    - update the right max elevation with the current right elevation
                - calculate the area: area += right max elevation - elevation of current right
                - decrement the right elevation position by 1
        :param height:
        :return:
        """
        left, right = 0, len(height) - 1
        left_max = right_max = area = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                area += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                area += right_max - height[right]
                right -= 1
        return area

    def get_trapped_rain_water_area_(self, height: List[int]) -> int:
        """
        Approach: Using Stack
        Time Complexity: O(n)
        Space Complexity: O(n)
        Algorithm:
            - loop through the elevations
                - while stack is not empty and elevation of current > stack top value elevation
                    - top = store the stack top value
                    - pop the top value from stack
                    - if stack is empty
                        - come out of the while condition
                    - distance = current elevation position - stack top value - 1
                    - bounded height = minimum
                                        (
                                            elevation at current position,
                                            elevation of stack top value
                                        ) -
                                        elevation of previous stack top value
                    - area = area + distance * bounded height
                - push the current position to top of the stack
                - increment the current position
        :param height:
        :return:
        """
        area = current_position = 0
        from collections import deque
        stack = deque()

        while current_position < len(height):
            while stack and height[current_position] > height[stack[0]]:
                previous_positon = stack.popleft()
                if not stack:
                    break
                distance = current_position - stack[0] - 1
                bounded_height = min(height[current_position], height[stack[0]]) - height[previous_positon]
                area += distance * bounded_height
            stack.appendleft(current_position)
            current_position += 1
        return area

    def get_trapped_rain_water_area__(self, height: List[int]) -> int:
        """
        Approach: Dynamic Programming
        Time Complexity: O(n)
        Space Complexity: O(n)
        :param height:
        :return:
        """
        if not height:
            return 0

        size = len(height)
        left_max = [0 for _ in range(size)]
        right_max = [0 for _ in range(size)]
        left_max[0], right_max[-1], area = height[0], height[-1], 0

        for i in range(1, size):
            left_max[i] = max(height[i], left_max[i - 1])
        for i in range(size - 2, -1, -1):
            right_max[i] = max(height[i], right_max[i + 1])
        for i in range(1, size):
            area += min(left_max[i], right_max[i]) - height[i]

        return area


if __name__ == "__main__":
    elevation_map = ElevationMap()
    print(elevation_map.get_trapped_rain_water_area__([0, 10, 0, 1, 3]))
    print(elevation_map.get_trapped_rain_water_area__([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(elevation_map.get_trapped_rain_water_area_([0, 10, 0, 1, 3]))
    print(elevation_map.get_trapped_rain_water_area_([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(elevation_map.get_trapped_rain_water_area([0, 10, 0, 1, 3]))
    print(elevation_map.get_trapped_rain_water_area([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))


