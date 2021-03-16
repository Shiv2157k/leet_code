from typing import List


class Songs:

    def song_pair_in_duration(self, time: List[int]) -> int:
        """
        Approach: Use array to store frequencies
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param time:
        :return:
        """
        remainders = [0] * 60
        result = 0
        for t in time:
            if t % 60 == 0:  # case 1: a % 60 == 0 and b % 60 == 0
                result += remainders[0]
            else:  # case 2: b = 60 - a % 60
                result += remainders[60 - t % 60]
            # update the frequency
            remainders[t % 60] += 1
        return result


if __name__ == "__main__":
    songs = Songs()
    print((songs.song_pair_in_duration([30, 20, 150, 100, 40])))
    print((songs.song_pair_in_duration([60, 60, 60])))
