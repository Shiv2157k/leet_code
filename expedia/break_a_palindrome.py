class Palindrome:

    def break_it(self, pal: str) -> str:
        """
        Conditions:
        -----------
        1. If length of palindrome is one return empty string.
        2. If even length string, we found a char that is not "a" replace it
           with a and return.
        3. If odd len string, find a char that is not "a" and if it is not middle of
           string replace with "a"
        4. If all "a" in string, replace the last char with b.
        Approach: String manipulation
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param pal:
        :return:
        """
        if len(pal) == 1:
            return ""

        p1, p2 = 0, len(pal) - 1

        while p1 < p2:

            if pal[p1] != "a":
                pal = pal[:p1] + "a" + pal[p1 + 1:]
                return pal
            p1 += 1
            p2 -= 1

        return pal[:-1] + "b"


if __name__ == "__main__":
    palindrome = Palindrome()
    print(palindrome.break_it("aaaa"))
    print(palindrome.break_it("aba"))
    print(palindrome.break_it("a"))
    print(palindrome.break_it("bb"))
    print(palindrome.break_it("aa"))