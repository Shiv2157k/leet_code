from typing import List


class CircularTrack:

    def most_visited(self, n: int, rounds: List[int]) -> List[int]:
        """
        Approach: Brute Force
        Time Complexity :O(N^2)
        Space Complexity: O(N)
        :param n:
        :param rounds:
        :return:
        """

        counter = [0] * (n + 1)

        start = rounds[0]
        counter[start] += 1

        for i in range(1, len(rounds)):
            end = rounds[i]

            while start != end:
                start = (start % n) + 1
                counter[start] += 1
            start = end

        most = max(counter)
        result = []

        for i in range(1, len(counter)):
            if counter[i] == most:
                result.append(i)
        return result


if __name__ == "__main__":
    circular_track = CircularTrack()
    print(circular_track.most_visited(4, [1, 3, 1, 2]))
    print(circular_track.most_visited(n=7, rounds=[1, 3, 5, 7]))
