

class Integer:

    digits = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"),
        (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "VI"), (1, "I")
    ]

    def to_roman(self, num: int) -> str:
        """
        Approach: Greedy
        Time Complexity: O(1)
        Space Complexity: O(1)
        :param num:
        :return:
        """
        romans = []

        for value, symbol in self.digits:
            if num == 0:
                break

            # count, num = num // value, num % value
            count, num = divmod(num, value)
            romans.append(symbol * count)
        return "".join(romans)


if __name__ == "__main__":

    integer = Integer()
    print(integer.to_roman(1994))
    print(integer.to_roman(3))
    print(integer.to_roman(58))
    print(integer.to_roman(3999))
    print(integer.to_roman(1111))