from typing import List


class Intervals:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Approach: Connected Components
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param intervals:
        :return:
        """
        intervals.sort(key=lambda a: a[0])
        n = 1
        while n < len(intervals):
            if intervals[n][0] <= intervals[n - 1][1]:
                intervals[n - 1][1] = max(intervals[n - 1][1], intervals[n][1])
                intervals.pop(n)
            else:
                n += 1
        return intervals


if __name__ == "__main__":
    interval = Intervals()
    print(interval.merge([[1, 3], [2, 8], [10, 11], [13, 19]]))