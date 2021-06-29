class Palindrome:

    def total_substrings_(self, s: str) -> int:
        """
        Approach: DP
        Time Complexity: O(N^2)
        Space Complexity: O(N^2)
        :param s:
        :return:
        """
        res, n = 0, len(s)

        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1
            res += 1

        for col in range(1, n):
            for row in range(col):

                # 2 letter palindrome
                if row == col - 1 and s[col] == s[row]:
                    dp[row][col] = 1
                    res += 1
                elif dp[row + 1][col - 1] == 1 and s[col] == s[row]:
                    dp[row][col] = 1
                    res += 1
        return res

    def total_subtrings(self, s: str) -> int:
        """
        Approach: Expand Center
        Time Complexity: O(N^2)
        Space Complexity: O(1)
        :param s:
        :return:
        """
        total_palindromes = 0

        def expand_center(left: int, right: int) -> int:
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                count += 1
            return count

        for i in range(len(s)):
            total_palindromes += expand_center(i, i)
            total_palindromes += expand_center(i, i + 1)
        return total_palindromes


if __name__ == "__main__":
    palindromes = Palindrome()
    print(palindromes.total_subtrings("axbobxa"))
    print(palindromes.total_substrings_("axbobxa"))
