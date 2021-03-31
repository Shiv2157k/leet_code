

class Integer:

    def reverse(self, n: int) -> int:
        """
        Approach: Pop and Push
        Time Complexity: O(log(x)) roughly log10 base x integers
        Space Complexity: O(1)
        :param n:
        :return:
        """

        result, sign = 0, 1

        if n < 0:
            n = -n
            sign = -1

        while n:
            result = result * 10 + n % 10
            n //= 10
        return 0 if result > 2**31 else result * sign


if __name__ == "__main__":
    integer = Integer()
    print(integer.reverse(989))
    print(integer.reverse(-989))
    print(integer.reverse(238298392328329232382))
    print(integer.reverse(1234))
    print(integer.reverse(-1234))