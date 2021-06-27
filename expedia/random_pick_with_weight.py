from random import random
from typing import List


class Weight:

    def __init__(self, w: List[int]):
        """
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param w:
        """
        self.prefix_sum = [w[0]]
        for idx in range(1, len(w)):
            self.prefix_sum.append(self.prefix_sum[-1] + w[idx])
        self.total_sum = self.prefix_sum[-1]

    def random_pick(self):
        """
        Time Complexity: O(N)
        Space Complexity: O(1)
        :return:
        """
        target = self.total_sum * random()
        for i, curr_sum in enumerate(self.prefix_sum):

            if target < curr_sum:
                return i

    def random_pick_advanced(self):
        """
        Time Complexity: O(log N)
        Space Complexity: O(1)
        :return:
        """
        target = self.total_sum * random()
        left, right = 0, len(self.prefix_sum)

        while left < right:
            pivot = left + (right - left) // 2
            if target > self.prefix_sum[pivot]:
                left = pivot + 1
            else:
                right = pivot
        return left


if __name__ == "__main__":
    weight = Weight([1, 2, 3, 9])
    print(weight.random_pick())
    print(weight.random_pick())
    print(weight.random_pick_advanced())
    weights = Weight([1, 9, 11, 13])
    print(weights.random_pick_advanced())
    print(weights.random_pick_advanced())