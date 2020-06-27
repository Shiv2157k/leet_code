

class Power:

    def get_power(self, x: int, n: int) -> float:
        """
        Approach: Fast Power Iterative with right shift
        and bit-wise "AND" operator.
        Time Complexity: O(log n)
        Space Complexity: O(1)
        :param x:
        :param n:
        :return:
        """
        m, value = abs(n), 1.0
        while m:
            if m & 1:
                value *= x
            x *= x
            m >>= 1
        return value if n >= 0 else 1 / value

    def get_power_(self, x: int, n: int) -> float:
        """
        Approach: Fast Power Iterative
        Time Complexity: O(log n)
        Space Complexity: O(1)
        :param x:
        :param n:
        :return:
        """
        m, value = abs(n), 1.0
        while m:
            if m % 2:
                value *= x
            x *= x
            m //= 2
        return value if n >= 0 else 1 / value


if __name__ == "__main__":
    power = Power()
    print(power.get_power(2, 3))
    print(power.get_power_(2, 3))
    print(power.get_power(25, 2))
    print(power.get_power_(25, 2))