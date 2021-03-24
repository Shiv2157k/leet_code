class Palindrome:

    def make_non_palindrome(self, pal: str) -> str:
        """
        Approach: Greedy
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param pal:
        :return:
        """
        p1, p2 = 0, len(pal) - 1
        while p1 < p2:

            if pal[p1] != "a":
                pal = pal[:p1] + "a" + pal[p1 + 1:]
                return pal
            p1 += 1
            p2 -= 1
        if len(pal) == 1:
            return ""
        return pal[:-1] + "b"


if __name__ == "__main__":
    palindrome = Palindrome()
    print(palindrome.make_non_palindrome(
        "aabaa"
    ))
    print(palindrome.make_non_palindrome(
        "aaaaa"
    ))
    print(palindrome.make_non_palindrome(
        "b"
    ))
    print(palindrome.make_non_palindrome(
        "aaa"
    ))
    print(palindrome.make_non_palindrome(
        "abaaba"
    ))