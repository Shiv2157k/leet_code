from typing import List


class Interval:

    def merge_overlaps(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        i = 1
        while i < len(intervals):
            if intervals[i][0] <= intervals[i - 1][1]:
                intervals[i - 1][1] = max(intervals[i - 1][1], intervals[i][1])
                intervals.pop(i)
            else:
                i += 1
        return intervals

    def merge_overlaps_(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        output = []
        for interval in intervals:
            if not output or output[-1][1] < interval[0]:
                output.append(interval)
            else:
                output[-1][1] = max(output[-1][1], interval[1])
        return output


if __name__ == "__main__":
    interval = Interval()
    print(interval.merge_overlaps([[1, 3], [2, 6], [8, 11], [14, 15]]))
    print(interval.merge_overlaps_([[1, 3], [2, 6], [8, 11], [14, 15]]))
    print(interval.merge_overlaps([[1, 3], [2, 6], [5, 11], [14, 15]]))
    print(interval.merge_overlaps_([[1, 3], [2, 6], [5, 11], [14, 15]]))
    print(interval.merge_overlaps([[1, 6], [2, 6], [4, 11], [5, 15]]))
    print(interval.merge_overlaps_([[1, 6], [2, 8], [4, 11], [5, 15]]))