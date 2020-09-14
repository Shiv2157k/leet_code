class PatternMatcher:

    def is_match(self, string: str, pattern: str) -> bool:
        """
        Approach: Back tracking
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param string:
        :param pattern:
        :return:
        """
        s_len, p_len = len(string), len(pattern)
        s_idx = p_idx = 0
        star_idx = star_temp_idx = -1

        while s_idx < s_len:
            # ? or p[i] == s[i]
            if p_idx < p_len and pattern[p_idx] in ["?", string[s_idx]]:
                s_idx += 1
                p_idx += 1
            # pattern is "*" mark the
            # star index, string index
            elif p_idx < p_len and pattern[p_idx] == "*":
                star_idx = p_idx
                star_temp_idx = s_idx
                p_idx += 1
            # if not * encountered
            elif star_idx == -1:
                return False
            # back track from the star index
            else:
                p_idx = star_idx + 1
                s_idx = star_temp_idx + 1
                star_temp_idx = s_idx
        return all(x == "*" for x in pattern[p_idx:])

    def is_match_(self, string: str, pattern: str) -> bool:
        """
        Approach: Dynamic Programming
        Time Complexity: O(SP)
        Space Complexity: O(SP)
        :param string:
        :param pattern:
        :return:
        """

        s_len, p_len = len(string), len(pattern)
        dp = [[False] * (p_len + 1) for _ in range(s_len + 1)]

        # if the initial characters in the pattern are *
        # mark the recursion_memoization_dp[0][i] to True
        for i in range(1, p_len + 1):
            if pattern[i - 1] != "*":
                break
            dp[0][i] = True

        for i in range(1, s_len + 1):
            for j in range(1, p_len + 1):
                if pattern[j - 1] in ["?", string[i - 1]]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif pattern[j - 1] == "*":
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
        return dp[-1][-1]


if __name__ == "__main__":
    pattern_matcher = PatternMatcher()
    print(pattern_matcher.is_match_("adcbdk", "*a*b?k"))
    print(pattern_matcher.is_match("adcbdk", "*a*b?k"))