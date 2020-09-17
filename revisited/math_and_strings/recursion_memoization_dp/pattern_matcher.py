class PatternMatcher:

    def is_match(self, text: str, pattern: str) -> bool:
        """
        Approach: DP
        Time Complexity: O(TP)
        Space Complexity: O(TP)
        :param text:
        :param pattern:
        :return:
        """

        # dp[i][j] - i is string, j - internal which is pattern
        dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]
        # initialize the last value in 2d matrix to True
        # considering the two empty char from text and pattern
        dp[-1][-1] = True

        # Bottom approach of dp
        for i in range(len(text), -1, -1):
            for j in range(len(pattern) - 1, -1, -1):
                # get the first match
                # if text index is less than text length and
                # pattern[j] in text[i] or if it is "."
                first_match = i < len(text) and pattern[j] in {text[i], "."}
                # case with pattern *
                if j + 1 < len(pattern) and pattern[j + 1] == "*":
                    dp[i][j] = dp[i][j + 2] or (first_match and dp[i + 1][j])
                else:
                    dp[i][j] = first_match and dp[i + 1][j + 1]
        return dp[0][0]

    def is_match_(self, text: str, pattern: str) -> bool:
        """
        Approach: Recursion
        Time Complexity: O ((T + P) * 2 ^ (T + P / 2))
        Space Complexity: O (T^2 + P^2)
        :param text:
        :param pattern:
        :return:
        """

        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], "."}

        if len(pattern) >= 2 and pattern[1] == "*":
            return (self.is_match_(text, pattern[2:]) or \
                    (first_match and self.is_match_(text[1:], pattern)))
        else:
            return first_match and self.is_match_(text[1:], pattern[1:])


if __name__ == "__main__":
    pattern_matcher = PatternMatcher()
    print(pattern_matcher.is_match_("xaabyc", "xa*b.c"))
    print(pattern_matcher.is_match("xaabyc", "xa*b.c"))