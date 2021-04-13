

class Fraction:

    def greatest_common_divisor(self, numerator: int, denominator: int) -> int:
        """
        Calculates the gcd provided the numerator and denominator.
        :param numerator:
        :param denominator:
        :return:
        """
        while denominator:
            temp = denominator
            denominator = numerator % denominator
            numerator = temp
        return numerator

    def calculate(self, expression: str) -> str:
        """
        Approach: GCD
        Time Complexity: O(n + log(N*D))
        - n is length of expression.
        - N, D un-reduced numerator and denominator.
        Space Complexity: O(N)
        - numerator and denominator array.
        :param expression:
        :return:
        """

        if not expression:
            return "0/1"

        if expression[0] != "-":
            expression = "+" + expression

        # local variables to store numerator and denominator
        numerator, denominator = [], []
        # for keeping track of sign
        is_positive = True

        pointer = 0

        while pointer < len(expression):

            if expression[pointer] == "-":
                is_positive = False
            else:
                is_positive = True

            pointer += 1
            # append numerator
            num = 0
            while expression[pointer].isdigit():
                num = num * 10 + int(expression[pointer])
                pointer += 1
            numerator.append(num if is_positive else -num)

            pointer += 1

            # denominator
            den = 0
            while pointer < len(expression) and expression[pointer].isdigit():
                den = den * 10 + int(expression[pointer])
                pointer += 1
            denominator.append(den)

        # calculate the common denominator by multiplying all the denominators
        common_denominator = 1
        for den in denominator:
            common_denominator *= den

        # generator updated numerator with the help
        # of common denominator
        for i, (num, den) in enumerate(zip(numerator, denominator)):
            numerator[i] = num * common_denominator // den

        # sum up all the numerator
        total_num = 0
        for num in numerator:
            total_num += num

        # find the gcd
        gcd = self.greatest_common_divisor(total_num, common_denominator)

        numerator = total_num // gcd
        denominator = common_denominator // gcd

        return f"{numerator}/{denominator}"


if __name__ == "__main__":

    fraction = Fraction()
    print(fraction.calculate("-3/1+2/3-3/2+4/7+5/5"))
    print(fraction.calculate("-1/2+1/2"))
