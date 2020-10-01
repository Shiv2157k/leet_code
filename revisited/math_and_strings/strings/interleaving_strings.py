from typing import List


class Strings:

    def is_interleave(self, s1: str, i: int, s2: str, j: int, res: str, s3: str) -> bool:

        # base case
        if i == len(s1) and j == len(s2) and res == s3:
            return True
        ans = False

        if i < len(s1):
            ans = ans or self.is_interleave(s1, i + 1, s2, j, res + s1[i], s3)
        if j < len(s2):
            ans = ans or self.is_interleave(s1, i, s2, j + 1, res + s2[j], s3)
        return ans

    def is_inter_leaving__(self, s1: str, s2: str, s3: str):
        """
        Approach: Recursion
        Time Complexity: O(2^m + n)
        Space Complexity: O(m + n)
        :param s1:
        :param s2:
        :param s3:
        :return:
        """
        return self.is_interleave(s1, 0, s2, 0, "", s3)

    def memoization(self, s1: str, i: int, s2: str, j: int, s3: str, k: int, memo: List[List[int]]):

        # if you reach end of string s1
        if i == len(s1):
            return s2[j:] == s3[k:]
        # if you reach end of string s2
        if j == len(s2):
            return s1[i:] == s3[k:]
        # get the already existing value from memoization
        if memo[i][j] >= 0:
            return True if memo[i][j] == 1 else False

        ans = False

        if s1[i] == s3[k] and self.memoization(s1, i + 1, s2, j, s3, k + 1, memo) or s2[j] == s3[k] and self.memoization(s1, i, s2, j + 1, s3, k + 1, memo):
            ans = True

        memo[i][j] = 1 if ans else 0
        return ans

    def is_inter_leaving___(self, s1: str, s2: str, s3: str) -> bool:
        """
        Approach: Recursion with memoization
        Time Complexity: O(MN)
        Space Complexity: O(MN)
        :param s1:
        :param s2:
        :param s3:
        :return:
        """
        memo = [[-1] * len(s2) for _ in range(len(s2))]
        return self.memoization(s1, 0, s2, 0, s3, 0, memo)

    def _is_interleaving(self, s1: str, s2: str, s3: str) -> bool:
        """
        Approach: DP with 2D Matrix
        Time Complexity: O(MN)
        Space Complexity: O(MN)
        :param s1:
        :param s2:
        :param s3:
        :return:
        """
        s1_len, s2_len, s3_len = len(s1), len(s2), len(s3)
        # base case
        if s3_len != s1_len + s2_len:
            return False

        dp = [[True] * (len(s2) + 1) for _ in range(len(s1) + 1)]

        for i in range(1, len(s1) + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
        for j in range(1, len(s2) + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]
        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
        return dp[-1][-1]

    def is_interleaving(self, s1: str, s2: str, s3: str) -> bool:
        """
        Approach: DP with 1D matrix
        Time Complexity: O(MN)
        Space Complexity: O(N)
        :param s1:
        :param s2:
        :param s3:
        :return:
        """
        s1_len, s2_len, s3_len = len(s1), len(s2), len(s3)
        # base case
        if s3_len != s1_len + s2_len:
            return False

        dp = [True] * (s2_len + 1)
        for j in range(1, s2_len + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]

        for i in range(1, s1_len + 1):
            dp[0] = (dp[0] and s1[i - 1] == s3[i - 1])
            for j in range(1, s2_len + 1):
                dp[j] = (dp[j] and s1[i - 1] == s3[i + j - 1]) or (dp[j - 1] and s2[j - 1] == s3[i + j - 1])
        return dp[-1]


if __name__ == "__main__":
    string = Strings()
    print(string.is_inter_leaving__("aabcc", "dbbca", "aadbbcbcac"))
    string_1 = Strings()
    print(string_1.is_inter_leaving___("aabcc", "dbbca", "aadbbcbcac"))
    string_2 = Strings()
    print(string_2._is_interleaving("aabcc", "dbbca", "aadbbcbcac"))
    string_3 = Strings()
    print(string_3.is_interleaving("aabcc", "dbbca", "aadbbcbcac"))