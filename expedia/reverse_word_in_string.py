from typing import List
from collections import deque


class String:

    def reverse_words(self, s: str) -> str:
        """
        Approach: Deque
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param s:
        :return:
        """

        left, right = 0, len(s) - 1

        while left <= right and s[left] == " ":
            left += 1

        while left <= right and s[right] == " ":
            right -= 1

        word, d = [], deque()

        while left <= right:

            if s[left] == " " and word:
                d.appendleft("".join(word))
                word = []
            elif s[left] != " ":
                word.append(s[left])
            left += 1
        d.appendleft("".join(word))
        return " ".join(d)

    def trim_spaces(self, s: str):
        left, right = 0, len(s) - 1

        while left <= right and s[left] == " ":
            left += 1

        while left <= right and s[right] == " ":
            right -= 1

        output = []

        while left <= right:

            if s[left] != " ":
                output.append(s[left])
            elif output[-1] != " ":
                output.append(s[left])
            left += 1
        return output

    def reverse(self, l: List[str], left: int, right: int):

        while left < right:
            l[left], l[right] = l[right], l[left]
            left += 1
            right -= 1

    def reverse_each_word(self, l: List[str]):
        start = end = 0

        while start < len(l):

            while end < len(l) and l[end] != " ":
                end += 1

            self.reverse(l, start, end - 1)
            start = end + 1
            end += 1

    def reverse_words_(self, s: str) -> str:
        """
        Approach: Reverse whole string and reverse each word.
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param s:
        :return:
        """

        l = self.trim_spaces(s)

        self.reverse(l, 0, len(l) - 1)

        self.reverse_each_word(l)

        return "".join(l)


if __name__ == "__main__":
    string = String()
    print(string.reverse_words("the sky is blue"))
    print(string.reverse_words_("the sky is blue"))