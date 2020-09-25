from typing import List


class Interval:

    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        """
        Approach: Greedy
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param intervals:
        :param new_interval:
        :return:
        """
        new_start, new_end = new_interval
        index, n = 0, len(intervals)
        output = []

        # add all the intervals less than new start interval
        while index < n and new_start > intervals[index][0]:
            output.append(intervals[index])
            index += 1

        # merge or add the new interval
        if not output or output[-1][-1] < new_start:
            output.append(new_interval)
        else:
            output[-1][-1] = max(output[-1][-1], new_end)

        # add all the remaining and merge if necessary
        while index < n:
            interval = intervals[index]
            start, end = interval
            index += 1

            if output[-1][-1] < start:
                output.append(interval)
            else:
                output[-1][-1] = max(output[-1][-1], end)
        return output


if __name__ == "__main__":
    interval = Interval()
    print(interval.insert([[1, 3], [6, 9]], [2, 5]))
    print(interval.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
    print(interval.insert([], [5, 7]))
    print(interval.insert([[1, 5]], [2, 7]))