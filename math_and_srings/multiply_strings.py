

class Multiplication:

    def two_strings(self, num1: str, num2: str) -> str:

        number1 = number2 = 0
        for digit in num1:
            number1 = number1 * 10 + ord(digit) - ord("0")
        for digit in num2:
            number2 = number2 * 10 + ord(digit) - ord("0")
        return str(number1 * number2)

    def two_strings_(self, num1: str, num2: str) -> str:

        length1 = len(num1)
        length2 = len(num2)
        digits = [0] * (length1 + length2)
        for index1 in range(length1 - 1, -1, -1):
            for index2 in range(length2 - 1, -1, -1):
                index = index1 + index2
                total = digits[index + 1] + (ord(num1[index1]) - ord("0")) * (ord(num2[index2]) - ord("0"))
                digits[index] += total // 10
                digits[index + 1] = total % 10

        product = ''
        for digit in digits:
            if not product and digit == 0:
                continue
            product += str(digit)
        return product or "0"


if __name__ == "__main__":

    multiplication = Multiplication()
    print(multiplication.two_strings("25", "20"))
    print(multiplication.two_strings_("25", "20"))
    print(multiplication.two_strings("5", "25"))
    print(multiplication.two_strings_("5", "25"))
    print(multiplication.two_strings("25", "2"))
    print(multiplication.two_strings_("25", "2"))
    print(multiplication.two_strings("5", "2"))
    print(multiplication.two_strings_("5", "2"))
