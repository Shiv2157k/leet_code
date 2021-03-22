from typing import List


class KeyPad:

    def slowest_key(self, release_times: List[int], key_pressed: str) -> str:
        """
        Approach: Comparision
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param release_times:
        :param key_pressed:
        :return:
        """

        max_time = release_times[0]
        key = key_pressed[0]

        for i in range(len(release_times) - 1):
            if max_time < release_times[i + 1] - release_times[i]:
                max_time = release_times[i + 1] - release_times[i]
                key = key_pressed[i + 1]
            elif max_time == release_times[i + 1] - release_times[i]:
                if key < key_pressed[i + 1]:
                    key = key_pressed[i + 1]
        return key


if __name__ == "__main__":
    keypad =KeyPad()
    print(keypad.slowest_key(
        [9, 29, 49, 50], "cbcd"
    ))
    print(keypad.slowest_key(
        [12, 23, 36, 46, 62], "spuda"
    ))