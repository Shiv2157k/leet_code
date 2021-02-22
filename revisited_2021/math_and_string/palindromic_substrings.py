

class Palindrome:

    def number_of_palindromic_substring_(self, s: str) -> int:
        """
        Approach: DP
        Time Complexity: O(N^2)
        Space Complexity: O(N)
        :param s:
        :return:
        """
        substrings, n = 0, len(s)
        dp = [[0] * n for _ in range(n)]

        # mark diagonals to 1
        for idx in range(n):
            dp[idx][idx] = 1
            substrings += 1

        # start the dp
        for col in range(1, n):
            for row in range(col):
                # check for two letter palindrome
                if row == col - 1 and s[row] == s[col]:
                    dp[row][col] = 1
                    substrings += 1
                # to determine if substring is palindrome
                # -> if inner substring is palindrome
                # -> if outer characters match
                elif dp[row + 1][col - 1] == 1 and s[row] == s[col]:
                    dp[row][col] = 1
                    substrings += 1
        return substrings

    def number_of_palindromic_substring(self, s: str) -> int:
        """
        Approach: Expand Around the Center
        Time Complexity: O(N^2)
        Space Complexity: O(1)
        :param s:
        :return:
        """
        def expand_center(left: int, right: int) -> int:
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count

        substrings = 0
        for idx in range(len(s)):
            substrings += expand_center(idx, idx)
            substrings += expand_center(idx, idx + 1)
        return substrings


if __name__ == "__main__":
    palindrome = Palindrome()
    print(palindrome.number_of_palindromic_substring("aaa"))
    print(palindrome.number_of_palindromic_substring("malayalam"))
    print(palindrome.number_of_palindromic_substring_("aaa"))
    print(palindrome.number_of_palindromic_substring_("malayalam"))