

class Fraction:

    def to_decimal(self, numerator: int, denominator: int) -> str:
        """
        Approach: Long Division
        Time Complexity:
        Space Complexity:
        :param numerator:
        :param denominator:
        :return:
        1/6
        6)1(0.166
          0
          --
          10
           6
          ---
           40
           36
          ---
            40
            36
            ---
             4
        """
        # base case
        if numerator % denominator == 0:
            return str(numerator // denominator)
        sign = "" if numerator * denominator >= 0 else "-"
        numerator, denominator = abs(numerator), abs(denominator)
        res = sign + str(numerator // denominator) + "."
        numerator %= denominator
        idx, part = 0, ""
        seen = {numerator: idx}
        while numerator % denominator:
            numerator *= 10
            idx += 1
            rem = numerator % denominator
            part += str(numerator // denominator)
            if rem in seen:
                part = part[:seen[rem]] + "(" + part[seen[rem]:] + ")"
                return res + part
            seen[rem] = idx
            numerator = rem
        return res + part


if __name__ == "__main__":
    fraction = Fraction()
    print(fraction.to_decimal(1, 6))
    print(fraction.to_decimal(1, 2))
    print(fraction.to_decimal(2, 1))
    print(fraction.to_decimal(0, 1))
    print(fraction.to_decimal(-1, 6))