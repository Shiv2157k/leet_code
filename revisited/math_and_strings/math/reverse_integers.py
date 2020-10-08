class Integer:

    def reverse(self, num: int) -> int:
        """
        Approach: Push and Pop
        Time Complexity: O(log num)
        Space Complexity: O(1)
        :param num:
        :return:
        """

        rev, sign = 0, 1
        if num < 0:
            # make it positive
            num = -num
            sign = -1
        while num:
            # add the num remainder and multiply
            # with existing rev value with 10
            rev = rev * 10 + num % 10
            # truncate the given number from left
            # until it reaches 0
            num //= 10
        return 0 if rev > 2**31 else rev * sign


if __name__ == "__main__":
    integer = Integer()
    print(integer.reverse(123))
    print(integer.reverse(456730332))
    print(integer.reverse(9999000))
    print(integer.reverse(1234567890))
    print(integer.reverse(-2157))
    print(integer.reverse(97857373533539525357))
    print(integer.reverse(-978573735335357))