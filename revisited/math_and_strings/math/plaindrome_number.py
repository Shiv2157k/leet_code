class Number:

    def is_palindrome(self, num: int) -> bool:
        """
        Approach: Revert the half
        Time Complexity: O(log base 10 N)
        Space Complexity: O(1)
        :param num:
        :return:
        """

        # base case
        if num < 0 or (num % 10 == 0 and num != 0):
            return False

        half = 0
        while num > half:
            half = half * 10 + num % 10
            num //= 10
        return num == half or num == half // 10


if __name__ == "__main__":
    number = Number()
    print(number.is_palindrome(121))
    print(number.is_palindrome(11))
    print(number.is_palindrome(-121))
    print(number.is_palindrome(11211))
    print(number.is_palindrome(2442))
    print(number.is_palindrome(2157))