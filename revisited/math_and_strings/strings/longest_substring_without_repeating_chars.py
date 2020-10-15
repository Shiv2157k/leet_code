

class String:

    def longest_substring_without_repetition_(self, s: str) -> int:
        """
        Approach: Sliding Window using max fun
        Time Complexity: O(n)
        Space Complexity: O(m)
        :param s:
        :return:
        """

        mapper = {}
        left = max_len = 0
        for right, char in enumerate(s):
            if char in mapper:
                left = max(left, mapper[char] + 1)
            max_len = max(max_len, right - left + 1)
            mapper[char] = right
        return max_len

    def longest_substring_without_repetition(self, s: str) -> int:
        """
        Approach: Sliding Window
        Time Complexity: O(n)
        Space Complexity: O(m)
        :param s:
        :return:
        """
        mapper = {}
        left = max_len = 0
        for right, char in enumerate(s):
            if char in mapper:
                start = mapper[char] + 1
                if start > left:
                    left = start
            curr_len = right - left + 1
            if curr_len > max_len:
                max_len = curr_len
            mapper[char] = right
        return max_len

    def is_unique(self, s: str, start: int, end: int) -> bool:
        """
        Checks if the sequence is a unique one without repeating
        character.
        :param s:
        :param start:
        :param end:
        :return:
        """
        str_set = set()
        for i in range(start, end):
            ch = s[i]
            if ch in str_set:
                return False
            str_set.add(ch)
        return True

    def longest_substring_without_repeating(self, s: str) -> int:
        """
        Approach: Brute Force
        Time Complexity: O(n^3)
        Space Complexity: O(set length)
        :param s:
        :return:
        """
        if not s:
            return 0
        n, length = len(s), 0
        if n == 1:
            return 1

        for i in range(0, n - 1):
            for j in range(i + 1, n + 1):
                if self.is_unique(s, i, j):
                    length = max(length, j - i)
        return length


if __name__ == "__main__":
    string = String()
    print(string.longest_substring_without_repeating("pwwkew"))
    print(string.longest_substring_without_repeating("au"))
    print(string.longest_substring_without_repeating(""))
    print(string.longest_substring_without_repeating(" "))
    print(string.longest_substring_without_repeating("a"))
    print("======================================")
    print(string.longest_substring_without_repetition("pwwkew"))
    print(string.longest_substring_without_repetition("au"))
    print(string.longest_substring_without_repetition(""))
    print(string.longest_substring_without_repetition(" "))
    print(string.longest_substring_without_repetition("a"))
    print("======================================")
    print(string.longest_substring_without_repetition_("pwwkew"))
    print(string.longest_substring_without_repetition_("au"))
    print(string.longest_substring_without_repetition_(""))
    print(string.longest_substring_without_repetition_(" "))
    print(string.longest_substring_without_repetition_("a"))

