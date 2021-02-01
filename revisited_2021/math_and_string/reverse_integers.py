class Integer:

    def reverse(self, x: int) -> int:
        """
        Approach: Pop & Push digits and check back for overflow.
        Time Complexity: O(log(x))
        Space Complexity: O(1)
        :param x:
        :return:
        """

        rev, sign = 0, 1

        if x < 0:
            x, sign = -x, -1

        while x:
            rev = rev * 10 + x % 10
            x //= 10
        return 0 if x > 2**31 else rev * x