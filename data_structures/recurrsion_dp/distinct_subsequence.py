class Subsequence:

    def get_distinct_subsequence(self, string: str, target: str) -> int:
        """
        Approach: DP 1D
        Time Complexity: O(MN)
        Space Complexity: O(N)
        :param string:
        :param target:
        :return:
        """
        M, N = len(string), len(target)
        dp = [0 for _ in range(N)]

        for i in range(M - 1, -1, -1):
            prev = 1
            for j in range(N - 1, -1, -1):
                dp_old = dp[j]
                if string[i] == target[j]:
                    dp[j] += prev
                prev = dp_old
        return dp[0]

    def get_distinct_subsequence_(self, string: str, target: str) -> int:
        """
        Approach: DP 2-D
        Time Complexity: O(MN)
        Space Complexity: O(MN)
        :param string:
        :param target:
        :return:
        """
        M, N = len(string), len(target)
        dp = [[0] * (N + 1) for _ in range(M + 1)]

        for j in range(N + 1):
            dp[M][j] = 0

        for i in range(M + 1):
            dp[i][N] = 1

        for i in range(M - 1, -1, -1):
            for j in range(N - 1, -1, -1):
                dp[i][j] = dp[i + 1][j]
                if string[i] == target[j]:
                    dp[i][j] += dp[i + 1][j + 1]
        return dp[0][0]

    def get_distinct_subsequence__(self, string: str, target: str) -> int:
        """
        Approach: Recursion with memoization
        :param string:
        :param target:
        :return:
        """
        memo = {}

        def unique(i, j):
            M, N = len(string), len(target)

            # base case
            if M == i or N == j or M - i < N - j:
                return int(j == len(target))

            if (i, j) in memo:
                return memo[i, j]

            ans = unique(i + 1, j)

            if string[i] == target[j]:
                ans += unique(i + 1, j + 1)
            memo[i, j] = ans
            return ans

        return unique(0, 0)


if __name__ == "__main__":
    sub_sequence = Subsequence()
    print(sub_sequence.get_distinct_subsequence__("rabbbit", "rabbit"))
    print(sub_sequence.get_distinct_subsequence_("rabbbit", "rabbit"))
    print(sub_sequence.get_distinct_subsequence("rabbbit", "rabbit"))
    print(sub_sequence.get_distinct_subsequence__("babgbag", "bag"))
    print(sub_sequence.get_distinct_subsequence_("babgbag", "bag"))
    print(sub_sequence.get_distinct_subsequence("babgbag", "bag"))
