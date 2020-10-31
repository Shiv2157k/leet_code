from typing import List


class Intervals:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Approach: Sorting
        Time Complexity: O(N log N)
        Space Complexity: O(1)
        :param intervals:
        :return:
        """

        intervals.sort(key=lambda x: x[0])
        n = 1
        while n < len(intervals):
            if intervals[n][0] <= intervals[n - 1][1]:
                intervals[n - 1][1] = max(intervals[n][0], intervals[n - 1][1])
                intervals.pop(n)
            else:
                n += 1
        return intervals


if __name__ == "__main__":

    intervals_ = Intervals()
    print(intervals_.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))