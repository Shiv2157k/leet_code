

class PatternMatching:

    def is_match(self, text: str, pattern: str) -> bool:
        """
        Approach: Dynamic Programming Bottom-Up
        Time Complexity: O(TP)
        Space Complexity: O(TP)
        :param text:
        :param pattern:
        :return:
        """
        dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]
        dp[-1][-1] = True
        for i in range(len(text), -1, -1):
            for j in range(len(pattern) - 1, -1, -1):
                first_match = i < len(text) and pattern[j] in {text[i], "."}
                if j + 1 < len(pattern) and pattern[j + 1] == "*":
                    dp[i][j] = dp[i][j + 2] or first_match and dp[i + 1][j]
                else:
                    dp[i][j] = first_match and dp[i + 1][j + 1]
        return dp[0][0]

    def is_match_(self, text: str, pattern: str) -> bool:
        """
        Approach: Recursion
        :param text:
        :param pattern:
        :return:
        """
        if not pattern:
            return not text
        first_match = bool(text) and pattern[0] in {text[0], "."}

        if len(pattern) >= 2 and pattern[1] == "*":
            return (self.is_match_(text, pattern[2:])) or first_match and self.is_match_(text[1:], pattern)
        else:
            return first_match and self.is_match_(text[1:], pattern[1:])


if __name__ == "__main__":
    pattern_matcher = PatternMatching()
    print(pattern_matcher.is_match_("aa", "a"))
    print(pattern_matcher.is_match_("aa", "a*"))
    print(pattern_matcher.is_match_("aab", "c*a*b"))
    print(pattern_matcher.is_match_("mississippi", "mis*is*p*"))
    print("-----------------------------")
    print(pattern_matcher.is_match("aa", "a"))
    print(pattern_matcher.is_match("aa", "a*"))
    print(pattern_matcher.is_match("aab", "c*a*b"))
    print(pattern_matcher.is_match("mississippi", "mis*is*p*"))
