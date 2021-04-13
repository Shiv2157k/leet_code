

class Fraction:

    def to_recurring_decimal(self, numerator: int, denominator: int) -> str:
        """
        Approach: Math + Hash Map
        Time Complexity:
        Space Complexity:
        :param numerator:
        :param denominator:
        :return:
        """

        # base case
        if numerator % denominator == 0:
            return str(numerator // denominator)
        # to find the sign
        sign = "" if numerator * denominator > 0 else "-"

        # make the numerator and denominator to absolute value
        numerator, denominator = abs(numerator), abs(denominator)
        # calculate the result before the decimal point
        result = sign + str(numerator // denominator) + "."
        # updated numerator
        numerator %= denominator
        # variables to keep track of repeating sequence
        part, index = "", 0
        seen = {numerator: index}

        # loop through either you find zero as remainder
        # or a recurring occurrence
        while numerator % denominator:
            # updated numerator
            numerator *= 10
            index += 1
            remainder = numerator % denominator
            part += str(numerator // denominator)
            if remainder in seen:
                part = part[:seen[remainder]] + "(" + part[seen[remainder]:] + ")"
                return result + part
            numerator = remainder
            seen[remainder] = index
        return result + part


if __name__ == "__main__":

    fraction = Fraction()
    print(fraction.to_recurring_decimal(1, 2))
    print(fraction.to_recurring_decimal(2, 1))
    print(fraction.to_recurring_decimal(4, 333))
    print(fraction.to_recurring_decimal(2, 3))