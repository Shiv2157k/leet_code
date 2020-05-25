

class ReverseInteger:

    def reverse_integer(self, num):
        """
        Approach: Using String
        :param num:
        :return:
        """
        reverse = int(str(abs(num))[::-1])
        return (-reverse if num < 0 else reverse) if reverse.bit_length() < 32 else 0

    def reverse_integer_math(self, num):
        """
        Approach: Using Math
        :param num:
        :return:
        """
        reverse, sign = 0, 1
        if num < 0:
            num = -num
            sign = -1
        while num:
            reverse = reverse * 10 + num % 10
            num //= 10
        return 0 if reverse > 2**31 else reverse * sign


if __name__ == "__main__":
    res = ReverseInteger()
    print(res.reverse_integer(-123))
    print(res.reverse_integer_math(-123))