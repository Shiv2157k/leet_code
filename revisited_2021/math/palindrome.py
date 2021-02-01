

class Integer:

    def is_palindrome(self, x: int) -> bool:
        """
        Revert half of the number.
        Time Complexity: O(log10(x))
        Space Complexity: O(1)
        :param x:
        :return:
        """
        # validation
        if x < 0 or (x % 10 == 0 and x!= 0):
            return False
        half = 0
        while x > half:
            half = half * 10 + x % 10
            x //= 10
        return x == half or x == half // 10