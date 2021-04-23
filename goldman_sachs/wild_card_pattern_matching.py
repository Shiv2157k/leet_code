class WildCardPatternMatcher:

    def __init__(self):
        self.memo = {}

    def remove_star_duplicates(self, p: str) -> str:
        """
        :param p:
        :return:
        """
        filtered_pattern = [p[0]]

        for char in p[1:]:
            if filtered_pattern[-1] != "*" or (filtered_pattern[-1] == "*" and char != "*"):
                filtered_pattern.append(char)
        return "".join(filtered_pattern)

    def helper(self, s: str, p: str) -> bool:
        """
        :param s:
        :param p:
        :return:
        """
        if (s, p) in self.memo:
            return self.memo[(s, p)]

        if p == s or p == "*":
            self.memo[(s, p)] = True
        elif not p or not s:
            self.memo[(s, p)] = False
        elif p[0] == s[0] or p[0] == "?":
            self.memo[(s, p)] = self.helper(s[1:], p[1:])
        elif p[0] == "*":
            self.memo[(s, p)] = self.helper(s[1:], p) or self.helper(s, p[1:])
        else:
            self.memo[(s, p)] = False
        return self.memo[(s, p)]

    def is_match_(self, s: str, p: str) -> bool:
        """
        Approach: Recursion with memoization
        Time Complexity:
        Space Complexity:
        :param s:
        :param p:
        :return:
        """
        self.memo = {}
        p = self.remove_star_duplicates(p)
        return self.helper(s, p)

    def is_match_dp(self, s: str, p: str) -> bool:
        """
        Approach: DP
        Time Complexity: O(MN)
        Space Complexity: O(MN)
        :param s:
        :param p:
        :return:
        """
        # base cases
        if s == p or p == "*":
            return True
        if s == "" or p == "":
            return False

        # filter the un-necessary stars
        p = self.remove_star_duplicates(p)
        s_len, p_len = len(s), len(p)

        dp = [[False] * (p_len + 1) for _ in range(s_len + 1)]

        dp[0][0] = True

        for i in range(1, p_len + 1):
            if p[i - 1] != "*":
                break
            dp[0][i] = True

        for i in range(1, s_len + 1):
            for j in range(1, p_len + 1):
                if p[j - 1] == "?" or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == "*":
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
        return dp[-1][-1]


if __name__ == "__main__":

    wild_card_pattern_matcher = WildCardPatternMatcher()
    print(wild_card_pattern_matcher.is_match_("adceb", "*a*b"))
    print(wild_card_pattern_matcher.is_match_dp("adceb", "*a*b"))

    print(wild_card_pattern_matcher.is_match_("adceb", "*a**b"))
    print(wild_card_pattern_matcher.is_match_dp("adceb", "*a**b"))

    print(wild_card_pattern_matcher.is_match_("adcebc", "*a*b"))
    print(wild_card_pattern_matcher.is_match_dp("adcebc", "*a*b"))

