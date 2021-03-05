from typing import List


class PairOfSongs:

    def total(self, times: List[int]) -> int:
        """
        Approach: Storing frequency in an array
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param times:
        :return:
        """
        remainders = [0] * 60
        # alternative
        # from collections import defaultdict
        # remainders = defaultdict(int)
        pairs = 0
        for time in times:
            if time % 60 == 0: # i.e., case 1: a % 60 == 0 & b % 60 = 0
                pairs += remainders[0]
            else: # case 2: b % 60 = 60 - a % 60
                pairs += remainders[60 - time % 60]
            # update the frequency
            remainders[time % 60] = 1
        return pairs


if __name__ == "__main__":
    pair_of_songs = PairOfSongs()
    print(pair_of_songs.total([30, 40, 60, 20, 100]))
    print(pair_of_songs.total([60, 60, 60, 60, 60]))
    print(pair_of_songs.total([60]))