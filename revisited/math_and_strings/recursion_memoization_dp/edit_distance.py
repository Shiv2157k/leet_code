

class EditDistance:

    def get_min_edits(self, word_1: str, word_2: str) -> int:
        """
        Approach: DP
        Time Complexity: O(w1w2)
        Space Complexity: O(w1w2)
        :param word_1:
        :param word_2:
        :return:
        """

        w1, w2 = len(word_1), len(word_2)

        if w1 * w2 == 0:
            return w1 + w2

        dp = [[0] * (w2 + 1) for _ in range(w1 + 1)]

        # init distances
        for i in range(w1 + 1):
            dp[i][0] = i
        for i in range(w2 + 1):
            dp[0][i] = i

        for i in range(1, w1 + 1):
            for j in range(1, w2 + 1):
                left = dp[i][j - 1] + 1
                up = dp[i - 1][j] + 1
                diagonal = dp[i - 1][j - 1]
                if word_1[i - 1] != word_2[j - 1]:
                    diagonal += 1
                dp[i][j] = min(left, up, diagonal)
        return dp[w1][w2]


if __name__ == "__main__":
    edit_distance = EditDistance()
    print(edit_distance.get_min_edits("horse", "ros"))
    print(edit_distance.get_min_edits("abcdef", "azced"))
    print(edit_distance.get_min_edits("intention", "execution"))