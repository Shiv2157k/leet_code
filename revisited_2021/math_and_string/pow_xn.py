

class Power:

    def result(self, x: float, n: float) -> float:
        """
        Approach: Iterative
        Time Complexity: O(log N)
        Space Complexity: O(1)
        :param x:
        :param n:
        :return:
        """
        ans, m = 1.0, abs(n)
        while m:
            if m % 2:
                ans *= x
            x *= x
            m //= 2
        return ans if n > 0 else 1/ans


if __name__ == "__main__":
    power = Power()
    print(power.result(2.0, 3.0))
    print(power.result(2.0, 4.0))
    print(power.result(2.0, -3.0))
