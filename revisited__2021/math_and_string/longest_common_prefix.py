class String:

    def longest_common_prefix_(self, s: str) -> str:
        """
        Approach: Linear
        Time Complexity: O(N + M)
        Space Complexity: O(1)
        :param s:
        :return:
        """
        if len(s) < 1:
            return ""

        min_word, max_word = s[0], s[0]

        for word in s:
            if min_word > word:
                min_word = word
            if max_word < word:
                max_word = word

        length = min(len(min_word), len(max_word))
        index = 0

        for i in range(length):
            if min_word[i] == max_word[i]:
                index += 1
            else:
                return min_word[:index]
        return min_word[:index]

    def longest_common_prefix(self, s: str) -> str:
        """
        Approach: Binary Search
        Time Complexity: O(S log m)
        S - sum of all characters in al strings
        takes log m iterations,
        for each S -> m * n comparisons
        Space Complexity: O(1)
        :param s:
        :return:
        """

        if not s:
            return ""
        min_str = min(s, key=len)
        left, right = 0, len(min_str) - 1

        while left <= right:
            pivot = left + (right - left) // 2
            prefix = s[0][:pivot]

            if all(ch.startswith(prefix) for ch in s[1:]):
                left += 1
            else:
                right -= 1
        return s[0][:(left + right) // 2]


if __name__ == "__main__":
    string = String()
    print(string.longest_common_prefix(["flower", "flow", "flight"]))
    print(string.longest_common_prefix_(["flower", "flow", "flight"]))