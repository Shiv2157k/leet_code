class Palindrome:

    def expand_center(self, s: str, left: int, right: int) -> int:

        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    def longest_substring(self, s: str) -> str:
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

        for i in range(len(s)):

            odd_len = self.expand_center(s, i, i)
            even_len = self.expand_center(s, i, i + 1)

            length = max(odd_len, even_len)

            if length > right - left:
                left = i - ((length - 1) // 2)
                right = i + length // 2
        return s[left: right + 1]


if __name__ == "__main__":

    palindrome = Palindrome()
    print(palindrome.longest_substring("bababg"))
    print(palindrome.longest_substring("cbbd"))
    print(palindrome.longest_substring("a"))
    print(palindrome.longest_substring("malayalam"))