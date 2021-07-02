from typing import List
from heapq import heappush, heappop


class MeetingRooms:

    def minimum_rooms_required(self, intervals: List[List[int]]) -> int:
        """
        Approach: Heap / Priority Queue
        Time Complexity: O(N log N)
        Space Complexity: O(N)
        :param intervals:
        :return:
        """
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[0])

        # store the end intervals
        # for checking overlaps and non overlaps
        rooms_required = []
        heappush(rooms_required, intervals[0][1])

        for interval in intervals[1:]:
            # pop the non overlap
            if interval[0] >= rooms_required[0]:
                heappop(rooms_required)
            # for overlap
            heappush(rooms_required, interval[1])
        return len(rooms_required)


if __name__ == "__main__":
    meeting_room = MeetingRooms()
    print(meeting_room.minimum_rooms_required(
        [[0, 30], [5, 10], [15, 20]]
    ))
    print(meeting_room.minimum_rooms_required(
        [[7, 10], [2, 4]]
    ))