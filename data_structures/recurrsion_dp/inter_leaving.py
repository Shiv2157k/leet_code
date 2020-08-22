from typing import List


class InterLeaving:

    def is_inter_leaving_string(self, str1: str, str2: str, str3: str) -> bool:
        """
        Approach: DP 1D Array
        Time Complexity: O(MN)
        Space Complexity: O(N)
        :param str1:
        :param str2:
        :param str3:
        :return:
        """
        len1, len2, len3 = len(str1), len(str2), len(str3)
        if len1 + len2 == len3:
            return False
        dp = [True] * (len2 + 1)

        for j in range(1, len2 + 1):
            dp[j] = dp[j - 1] and str2[j - 1] == str3[j - 1]

        for i in range(1, len1 + 1):
            dp[0] = dp[0] and str1[i - 1] == str3[i - 1]
            for j in range(1, len2 + 1):
                dp[j] = (dp[j] and str2[j - 1] == str3[i + j - 1]) or (dp[i] and str1[i - 1] == str3[i + j - 1])
        return dp[-1][-1]

    def is_inter_leaving_string_(self, str1: str, str2: str, str3: str) -> bool:
        """
        Approach: DP 2D Array
        Time Complexity: O(MN)
        Space Complexity: O(MN)
        :param str1:
        :param str2:
        :param str3:
        :return:
        """
        s1_len, s2_len, s3_len = len(str1), len(str2), len(str3)

        if s3_len != s1_len + s2_len:
            return False

        dp = [[True] * (s2_len + 1) for _ in range(s1_len + 1)]

        for i in range(1, s1_len + 1):
            dp[i][0] = dp[i - 1][0] and str1[i - 1] == str3[i - 1]
        for j in range(1, s2_len + 1):
            dp[0][j] = dp[0][j - 1] and str2[j - 1] == str3[j - 1]
        for i in range(1, s1_len + 1):
            for j in range(1, s2_len + 1):
                dp[i][j] = (dp[i - 1][j] and str1[i - 1] == str3[i + j - 1]) or (
                            dp[i][j - 1] and str2[j - 1] == str3[i + j - 1])
        return dp[-1][-1]


if __name__ == "__main__":
    interleaving = InterLeaving()
    print(interleaving.is_inter_leaving_string("aabcc", "dbbca", "aadbbcbcac"))
    print(interleaving.is_inter_leaving_string_("aabcc", "dbbca", "aadbbcbcac"))
