class Power:

    def of_x_and_n(self, x: float, n: int) -> float:
        """
        Approach:
        Time Complexity:
        Space Complexity:
        :param x:
        :param n:
        :return:
        """

        m, res = abs(n), 1.0

        while m:
            if m % 2 == 1:
                res *= x
            x *= x
            m //= 2
        return res if n > 0 else 1 / res

    def of_x_and_n_(self, x: float, n: int) -> float:
        """
        Approach:
        Time Complexity:
        Space Complexity:
        :param x:
        :param n:
        :return:
        """
        m, res = abs(n), 1.0
        while m:
            if m & 1:
                res *= x
            x *= x
            m >>= 1
        return res if n > 0 else 1 / res


if __name__ == "__main__":
    power = Power()
    print(power.of_x_and_n(x=2.100, n=3))
    print(power.of_x_and_n(x=2.0, n=-2))

    print(power.of_x_and_n_(x=2.100, n=3))
    print(power.of_x_and_n_(x=2.0, n=-2))