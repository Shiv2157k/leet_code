from typing import List


class WildCard:

    def is_match(self, string: str, pattern: str) -> bool:
        """
        Approach: Back Tracking
        Time Complexity: O(SP)
        Space Complexity: O(1)
        :param string:
        :param pattern:
        :return:
        """
        s_len, p_len = len(string), len(pattern)
        s_idx = p_idx = 0
        star_idx = s_temp_idx = -1

        while s_idx < s_len:
            # if pattern char is equal to string char
            # or patter is equal to "?"
            if pattern[p_idx] in [string[s_idx], "?"]:
                s_idx += 1
                p_idx += 1
            # if pattern char is "*"
            elif p_idx < p_len and pattern[p_idx] == "*":
                # check the situation when * matches no characters
                star_idx = p_idx
                s_temp_idx = s_idx
                p_idx += 1
            # if pattern character is not equal to string character
            # or pattern is used up and there was no "*" character
            # in pattern
            elif star_idx == -1:
                return False
            # if pattern character is not equal to string character
            # or pattern is used up and there was "*" character in
            # pattern before
            else:
                # Backtrack: check the situation
                # when "*" matches one more character
                p_idx = star_idx + 1
                s_idx = s_temp_idx + 1
                s_temp_idx = s_idx

        # the remaining characters in pattern should all be "*" characters.
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
        s_len = len(string)
        p_len = len(pattern)

        dp = [[False] * (p_len + 1) for _ in range(s_len + 1)]
        dp[0][0] = True

        for idx in range(1, p_len + 1):
            if pattern[idx - 1] != "*":
                break
            dp[0][idx] = True

        for s in range(1, s_len + 1):
            for p in range(1, p_len + 1):

                if pattern[p - 1] in {string[s - 1], "?"}:
                    # grab the value from diagonal
                    dp[s][p] = dp[s - 1][p - 1]
                elif pattern[p - 1] == "*":
                    dp[s][p] = dp[s - 1][p] or dp[s][p - 1]
        return dp[-1][-1]


if __name__ == "__main__":

    wild_card = WildCard()
    print(wild_card.is_match_("adcebdk", "*a*b?k"))
    print(wild_card.is_match("adcebdk", "*a*b?k"))