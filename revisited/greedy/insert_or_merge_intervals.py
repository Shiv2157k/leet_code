from typing import List


class Intervals:

    def insert_or_merge(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        """
        Approach: Greedy
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param intervals:
        :param new_interval:
        :return:
        """
        new_start, new_end = new_interval
        index, length = 0, len(intervals)
        new_intervals = []

        # add intervals less than new interval
        while index < length and new_start > intervals[index][0]:
            new_intervals.append(intervals[index])
            index += 1

        # add new interval or merge if necessary
        if not new_intervals or new_start > new_intervals[-1][-1]:
            new_intervals.append(new_interval)
        else:
            new_intervals[-1][-1] = max(new_intervals[-1][-1], new_end)

        # add or merge the remaining intervals
        while index < length:
            interval = intervals[index]
            start, end = interval
            index += 1
            if new_intervals[-1][-1] < start:
                new_intervals.append(interval)
            else:
                new_intervals[-1][-1] = max(new_intervals[-1][-1], end)
        return new_intervals


if __name__ == "__main__":
    i = Intervals()
    print(i.insert_or_merge([[1, 3], [6, 9]], [2, 5]))
    print(i.insert_or_merge([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
    print(i.insert_or_merge([], [5, 7]))

