

class Palindrome:

    def is_palindrome(self, num: int) -> bool:
        """
        Approach: Revert to half
        :param num:
        :return:
        """
        if num < 0 or (num % 10 == 0 and num != 0):
            return False

        half = 0
        while num > half:
            half = half * 10 + num % 10
            num //= 10
        return num == half or num == half // 10


if __name__ == "__main__":
    pal = Palindrome()
    print(pal.is_palindrome(112111))