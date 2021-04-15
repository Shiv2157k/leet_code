from typing import List


class Students:

    def height_position_changes(self, heights: List[int]) -> int:
        """
        Approach: Counting Sort
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param heights:
        :return:
        """

        height_freq = {}
        # height_freq = collections.defaultdict(int)
        for height in heights:
            # alternative
            # height_freq[height] = height_freq.get(height, 0) + 1
            if height in height_freq:
                height_freq[height] += 1
            else:
                height_freq[height] = 1

        removals = position = 0

        for height in heights:
            # increase the position for below case
            # alternative
            # while height_freq.get(position, 0) == 0:
            while position not in height_freq or height_freq[position] == 0:
                position += 1
            # if the current position and height is not matching
            # add increment the removal
            if position != height:
                removals += 1
            # decrement the freq
            height_freq[position] -= 1
        return removals


if __name__ == "__main__":
    students = Students()
    print(students.height_position_changes([1, 1, 4, 2, 1, 3]))