

class String:

    def max_substring_len_without_repeating(self, s: str) -> int:
        """
        Approach: Sliding Window Optimized
        Time Complexity: O(M)
        Space Complexity: O(min(M, N))
        Space Complexity Dictionary: O(M)
        :param s:
        :return:
        """

        if not s:
            return 0
        mapper = {}
        left = max_len = 0

        for right, char in enumerate(s):
            if char in mapper:
                left = max(left, mapper[char])
            max_len = max(max_len, right - left + 1)
            mapper[char] = right + 1
        return max_len


if __name__ == "__main__":
    string = String()
    print(string.max_substring_len_without_repeating("abcabcbb"))