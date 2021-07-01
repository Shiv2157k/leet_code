from typing import List
from collections import Counter


class Array:

    def least_number_of_unique_int(self, arr: List[int], k: int) -> int:
        """
        Approach: Hash Map
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param arr:
        :param k:
        :return:
        """

        num_freq = Counter(arr)
        occurence_freq, remaining = Counter(num_freq.values()), len(num_freq)

        for key in range(1, len(arr) + 1):

            if k >= key * occurence_freq[key]:
                k -= key * occurence_freq[key]
                remaining -= occurence_freq[key]
            else:
                return remaining - k // key
        return remaining


if __name__ == "__main__":
    array = Array()
    print(array.least_number_of_unique_int([4, 3, 1, 1, 3, 3, 2], 3))