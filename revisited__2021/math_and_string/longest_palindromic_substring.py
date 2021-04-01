class String:

    def expand_center(self, s: str, left: int, right: int) -> int:
        """
        :param s:
        :param l:
        :param r:
        :return:
        """
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    def longest_palindromic_substring(self, s: str) -> str:
        """
        Approach: Expand Center
        Time Complexity: O(N^2)
        Space Complexity: O(1)
        :param s:
        :return:
        """

        if not s or len(s) < 1:
            return ""
        left = right = 0

        for index in range(len(s)):

            odd_len = self.expand_center(s, index, index)
            even_len = self.expand_center(s, index, index + 1)

            length = max(odd_len, even_len)
            if length > left + right:
                left = index - (length - 1) // 2
                right = index + length // 2
        return s[left: right + 1]


if __name__ == "__main__":
    S = String()
    print(S.longest_palindromic_substring("aaa"))
    print(S.longest_palindromic_substring("aabaa"))
    print(S.longest_palindromic_substring("dbbbbc"))
    print(S.longest_palindromic_substring("dabadc"))
    print(S.longest_palindromic_substring("sdacad"))
    print(S.longest_palindromic_substring("a"))
    print(S.longest_palindromic_substring("aaba"))
    print(S.longest_palindromic_substring("aa"))
