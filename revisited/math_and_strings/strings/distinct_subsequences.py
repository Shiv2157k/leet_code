

class Subsequences:

    def get_distinct(self, string: str, target: str) -> int:
        """
        Approach: DP with 1D Array
        Time Complexity: O(MN)
        Space Complexity: O(M)
        :param string:
        :param target:
        :return:
        """
        s_len, t_len = len(string), len(target)
        if s_len * t_len == 0:
            return 0
        dp = [0] * t_len
        for i in range(s_len - 1, -1, -1):
            # At each step we start with last value in the row which
            # is always 1. Notice how we are starting the loop from
            # N - 1 instead of N like in previous solution.
            prev = 1
            for j in range(t_len - 1, -1, -1):
                # Record the current value in this cell so that we can
                # use it to calculate the value of dp[j - 1]
                old_dp = dp[j]
                # if the characters match, we add the result of next
                # recursion call (in this case, the value of a cell in
                # dp table)
                if string[i] == target[j]:
                    dp[j] += prev
                # Update the previous variable.
                prev = old_dp
        return dp[0]

    def get_distinct_(self, string: str, target: str) -> int:
        """
        Approach: DP with 2D array.
        Time Complexity: O(MN)
        Space Complexity: O(MN)
        :param string:
        :param target:
        :return:
        """
        s_len, t_len = len(string), len(target)
        if s_len * t_len == 0:
            return 0
        dp = [[0] * (t_len + 1) for _ in range(s_len + 1)]

        for i in range(s_len + 1):
            dp[i][t_len] = 1

        for i in range(s_len - 1, -1, -1):
            for j in range(t_len - 1, -1, -1):
                dp[i][j] = dp[i + 1][j]
                if string[i] == target[j]:
                    dp[i][j] += dp[i + 1][j + 1]
        return dp[0][0]

    def get_distinct__(self, string: str, target: str) -> int:
        """
        Approach: Recursion with memoization
        Time Complexity: O(M * N)
        Space Complexity: O(M * N)
        :param string:
        :param target:
        :return:
        """
        def unique_sub_sequences(i: int, j: int):
            # base case
            if i == s_len or j == t_len or s_len - i < t_len - j:
                return int(j == t_len)

            # check in cache
            if (i, j) in memo:
                return memo[i,j]

            # always run this recursion
            ans = unique_sub_sequences(i + 1, j)
            if string[i] == target[j]:
                ans += unique_sub_sequences(i + 1, j + 1)

            # store in the cache
            memo[i, j] = ans
            return ans
        memo = {}
        s_len, t_len = len(string), len(target)
        return unique_sub_sequences(0, 0)


if __name__ == "__main__":
    subsequences = Subsequences()
    print(subsequences.get_distinct__("rabbbit", "rabbit"))
    sub_sequences = Subsequences()
    print(sub_sequences.get_distinct_("rabbbit", "rabbit"))
    print(sub_sequences.get_distinct("rabbbit", "rabbit"))