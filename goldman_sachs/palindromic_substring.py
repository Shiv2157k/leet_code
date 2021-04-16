class Palindrome:

    def total_substrings_(self, s: str) -> int:
        """
        Approach: Expand Centers
        Time Complexity: O(N^2)
        Space Complexity: O(1)
        :param s:
        :return:
        """

        n = len(s)
        total_palindromes = 0

        def count_palindromes(left: int, right: int) -> int:
            counter = 0
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
                counter += 1
            return counter

        for i in range(n):
            # odd palindromes
            total_palindromes += count_palindromes(i, i)
            # even palindromes
            total_palindromes += count_palindromes(i, i + 1)
        return total_palindromes

    def total_substrings(self, s: str) -> int:
        """
        Approach: DP
        Time Complexity: O(N^2)
        Space Complexity: O(N^2)
        :param s:
        :return:
        """

        n = len(s)
        total_palindromes = 0

        # build the dp array
        dp = [[0] * n for _ in range(n)]
        # mark all the diagonals as palindrome by 1
        for i in range(n):
            dp[i][i] = 1
            total_palindromes += 1

        # loop through each column and row
        for column in range(1, n):
            for row in range(column):
                # case 1: palindrome with length 2
                # eg: 0 - 1, 1 - 2, 2 - 3...
                if row == column - 1 and s[row] == s[column]:
                    dp[row][column] = 1
                    total_palindromes += 1
                # case 2: length > 2 and internal substring inside needs to be palindrome
                elif dp[row + 1][column - 1] == 1 and s[row] == s[column]:
                    dp[row][column] = 1
                    total_palindromes += 1
        return total_palindromes


if __name__ == "__main__":
    palindrome = Palindrome()
    print(palindrome.total_substrings("abc"))
    print(palindrome.total_substrings("aaa"))
    print(palindrome.total_substrings("aabaaca"))
    print(palindrome.total_substrings_("abc"))
    print(palindrome.total_substrings_("aaa"))
    print(palindrome.total_substrings_("aabaaca"))



