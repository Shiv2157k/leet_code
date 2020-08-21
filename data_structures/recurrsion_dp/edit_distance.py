class Distance:

    def get_min_edits(self, word1: str, word2: str) -> int:
        """
        Approach: Dynamic Programming
        Time Complexity: O(nm)
        Space Complexity: O(nm)
        :param word1:
        :param word2:
        :return:
        """
        n, m = len(word1), len(word2)

        # base case
        if n * m == 0:
            return n + m

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = i
        for j in range(m + 1):
            dp[0][j] = j

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                left = dp[i][j - 1] + 1
                up = dp[i - 1][j] + 1
                diagonal = dp[i - 1][j - 1]
                if word1[i - 1] != word2[j - 1]:
                    diagonal += 1
                dp[i][j] = min(left, up, diagonal)
        return dp[n][m]


if __name__ == "__main__":
    distance = Distance()
    print(distance.get_min_edits("intention", "execution"))
    print(distance.get_min_edits("horse", "rose"))

