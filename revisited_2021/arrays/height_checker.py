from typing import List


class HeightChecker:

    def check(self, heights: List[int]) -> int:
        """
        Approach: Counting Sort
        Time Complexity: O(N)
        Space Complexity:: O(N)
        :param heights:
        :return:
        """
        from collections import Counter
        # counter = Counter(heights)
        counter = {}
        for height in heights:
            counter[height] = counter.get(height, 0) + 1
        i = 0
        removals = 0
        for height in heights:
            while counter.get(i, 0) == 0:
                i += 1
            if i != height:
                removals += 1
            counter[i] -= 1
        return removals


if __name__ == "__main__":
    height_checker = HeightChecker()
    print(height_checker.check([1, 2, 3, 4, 5, 6]))
    print(height_checker.check([1, 1, 4, 2, 1, 3]))
    print(height_checker.check([5, 4, 3, 2, 1]))
    print(height_checker.check([5, 1, 2, 3, 4]))