from typing import List


class String:

    def reverse(self, s: List[str]) -> str:
        """
        Approach: Two Pointers
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param s:
        :return:
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s


if __name__ == "__main__":
    string = String()
    print(string.reverse(["h", "e", "l", "l", "o"]))
    print(string.reverse(["m", "a", "l", "a", "y", "a", "l", "a", "m"]))
