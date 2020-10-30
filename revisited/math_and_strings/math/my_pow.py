

class Calculate:

    def power(self, x: float, n: int) -> float:
        """
        Approach: Recursion Optimized
        Time Complexity: O(log N)
        Space Complexity: O(1)
        :param x:
        :param n:
        :return:
        """
        # base cases
        if n == 0:
            return 1.0
        if n == 1:
            return x
        if n < 0:
            return self.power(1/x, -n)
        result = self.power(x*x, n // 2)
        if n % 2:
            result *= x
        return result

    def power_(self, x: float, n: int) -> float:
        """
        Approach: Iterative
        Time Complexity: O(log N)
        Space Complexity: O(1)
        :param x:
        :param n:
        :return:
        """
        m, result = abs(n), 1.0
        while m:
            if m % 2:
                result *= x
            x *= x
            m //= 2
        return result if n > 0 else 1 / result

    def power___(self, x: float, n: int) -> float:
        """
        Approach: Brute Force (Recursion)
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param x:
        :param n:
        :return:
        """
        # base cases
        if n == 0:
            return 1.0
        if n == 1:
            return x
        if n < 0:
            return self.power___(1/x, -n)
        result = 1.0
        for i in range(n):
            result *= x
        return result


if __name__ == "__main__":
    calculate = Calculate()
    calculate_ = Calculate()
    calculate__ = Calculate()
    print(calculate.power(2.0, 10))
    print(calculate_.power_(2.0, 10))
    print(calculate__.power___(2.0, 10))
    print(calculate.power(2.0, -2))
    print(calculate_.power_(2.0, -2))
    print(calculate__.power___(2.0, -2))
