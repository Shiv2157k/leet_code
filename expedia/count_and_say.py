from typing import List


class Integer:

    def count_and_say(self, n: int) -> str:
        """
        Approach: Iterative

        :param n:
        :return:
        """
        seq = ["1"]

        for digit in range(2, n + 1):
            next_seq = []
            digit_count = 1
            prev_digit = seq[0]

            for d in seq[1:]:

                if d == prev_digit:
                    digit_count += 1
                else:
                    next_seq.extend([str(digit_count), prev_digit])
                    digit_count = 1
                    prev_digit = d
            next_seq.extend([str(digit_count), prev_digit])
            seq = next_seq[:]
        return "".join(seq)

    def count_and_say_(self, n: int) -> str:
        """
        Approach: Recursion
        :param n:
        :return:
        """
        return "".join(self.build_pattern(n, ["1", "$"]))

    def build_pattern(self, n: int, seq: List[str]):

        if n == 1:
            return seq[:-1]

        next_seq = []
        prev_digit = seq[0]
        digit_count = 1

        for digit in seq[1:]:
            if prev_digit == digit:
                digit_count += 1
            else:
                next_seq.extend([str(digit_count), prev_digit])
                prev_digit = digit
                digit_count = 1
        next_seq.append("$")
        return self.build_pattern(n - 1, next_seq)


if __name__ == "__main__":
    integer = Integer()
    print(integer.count_and_say(4))
    print(integer.count_and_say_(4))