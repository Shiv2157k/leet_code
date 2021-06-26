class String:

    def smallest_divisor(self, s: str, t: str) -> int:
        """
        Time Complexity: O(N)
        :param s:
        :param t:
        :return:
        """

        fits = False
        concat = t
        mul = 1

        while len(concat) <= len(s):

            if concat != s:
                mul += 1
                concat = t * mul
            else:
                fits = True
                break
        if not fits:
            return -1

        for i in range(1, len(t) + 1):
            if t[:i] * (len(t) // i) == t:
                return i


if __name__ == "__main__":
    string = String()
    print(string.smallest_divisor("bcdbcdbcd", "bcdbcd"))
    print(string.smallest_divisor("bcdbcdbcdbcd", "bcdbcd"))
