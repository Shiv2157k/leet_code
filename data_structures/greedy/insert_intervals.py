from typing import List
from pprint import pprint


class Interval:

    def insert_or_merge(self, intervals: List[List[int]], new_interval: List[List[int]]):
        """
        Approach: Greedy Algorithm
        Time Complexity: O(N)
        Space Complexity: O(N)
        intervals: [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
        new_intervals: [4, 8]
        :param intervals:
        :param new_interval:
        :return:
        """

        # init what needed
        new_start, new_end = new_interval
        index, n = 0, len(intervals)
        output = []

        # add intervals less than the new interval
        while index < n and new_start > intervals[index][0]:
            output.append(intervals[index])
            index += 1

        # add or merge the new interval
        if output[-1][1]  < new_start:
            # add
            output.append(new_interval)
        else:
            # merge
            output[-1][-1] = max(output[-1][-1], new_end)

        # add or merge the rest of the intervals
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
    merged_interval = Interval()
    pprint(merged_interval.insert_or_merge([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
    pprint(merged_interval.insert_or_merge([[1, 3], [6, 9]], [2, 5]))