class Number:

    def is_palindrome(self, n: int) -> bool:
        """
        Approach: Compare Half
        Time Complexity: O(log base 10(N))
        Space Complexity: O(1)
        :param n:
        :return:
        """
        if n < 0 or (n % 10 == 0 and n != 0):
            return False
        half = 0
        while n > half:
            half = half * 10 + n % 10
            n //= 10
        return n == half or n == half // 10


if __name__ == "__main__":
    number = Number()
    print(number.is_palindrome(1221))
    print(number.is_palindrome(-1221))
    print(number.is_palindrome(0))
    print(number.is_palindrome(120))
    print(number.is_palindrome(1333333331))