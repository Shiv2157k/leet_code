from typing import List


class DailyTemperature:

    def get_day_difference_when_increased(self, temperatures: List[int]) -> List[int]:
        """
        Approach: Stack
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param temperatures:
        :return:
        """

        result = [0] * len(temperatures)
        stack = []

        for day, temp in enumerate(temperatures):

            while stack and temp > temperatures[stack[-1]]:
                prev_day = stack.pop()
                result[prev_day] = day - prev_day
            stack.append(day)
        return result


if __name__ == "__main__":
    daily_temperatures = DailyTemperature()
    print(daily_temperatures.get_day_difference_when_increased([73, 74, 75, 71, 69, 72, 76, 73]))
    print(daily_temperatures.get_day_difference_when_increased([30, 40, 50, 60]))
    print(daily_temperatures.get_day_difference_when_increased([30, 60, 90]))
