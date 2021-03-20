from typing import List


class People:

    def queue_reconstruction_by_height(self, people: List[List[int]]) -> List[int]:
        """
        Approach: Greedy
        Time Complexity: O(N^2) - O(N log N) Sorting O(K) for inserting
        Space Complexity: O(N)
        :param people:
        :return:
        """
        people.sort(key=lambda x: (-x[0], x[1]))
        queue = []
        for person in people:
            queue.insert(person[1], person)
        return queue


if __name__ == "__main__":
    p = People()
    print(p.queue_reconstruction_by_height(
        [
            [7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]
        ]
    ))
