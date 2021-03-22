import heapq
from typing import List


class MeetingRooms:

    def total_used(self, intervals: List[List[int]]) -> int:
        """
        Approach: Heap
        Time Complexity: O(N log N)
        Space Complexity: O(N)
        :param intervals:
        :return:
        """
        # validation
        if not intervals:
            return 0

        # sort the intervals based on start range
        intervals.sort(key=lambda interval: interval[0])

        free_rooms = []
        heapq.heappush(free_rooms, intervals[0][1])

        for interval in intervals[1:]:
            # if no over lap
            if interval[0] >= free_rooms[0]:
                heapq.heappop(free_rooms)
            # if over lap
            heapq.heappush(free_rooms, interval[1])
        return len(free_rooms)


if __name__ == "__main__":
    meeting_rooms = MeetingRooms()
    print(meeting_rooms.total_used(
        [
            [0, 30], [5, 10], [15, 20]
        ]
    ))
    print(meeting_rooms.total_used(
        [
            [7, 10], [2, 4]
        ]
    ))