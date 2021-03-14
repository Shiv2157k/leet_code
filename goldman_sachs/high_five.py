import heapq

from typing import List


class Students:

    def high_five(self, items: List[List[int]]):
        """
        Approach: Hash Map + Min Heap
        Time Complexity: O(log N)
        Space Complexity: O(N)
        :param items:
        :return:
        """
        average = dict()
        for student, score in items:
            if student not in average:
                average[student] = []
                heapq.heappush(average[student], score)
            else:
                if len(average[student]) < 5:
                    heapq.heappush(average[student], score)
                else:
                    heapq.heappushpop(average[student], score)
        return [[student, sum(scores) // 5] for student, scores in average.items()]


if __name__ == "__main__":
    students = Students()
    print(students.high_five(
        [
            [1, 91], [1, 92], [2, 93], [2, 97], [1, 60], [2, 77], [1, 65], [1, 87], [1, 100], [2, 100], [2, 76]
        ]
    ))
