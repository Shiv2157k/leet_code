from typing import List


class Number:

    def count_and_say(self, n: int) -> str:
        """
        Approach: Recursion
        Time Complexity: O(2** N)
        Space Complexity: O(2** N - 1)
        :param n:
        :return:
        """
        return "".join(self.next_sequence(n, ["1", "$"]))

    def next_sequence(self, n: int, prev_seq: List[str]):
        """
        Recursion
        :param n:
        :param prev_seq:
        :return:
        """
        # base case
        if n == 1:
            return prev_seq[:-1]
        next_seq = []
        prev_digit = prev_seq[0]
        digit_count = 1
        for digit in prev_seq[1:]:
            if digit == prev_digit:
                digit_count += 1
            else:
                next_seq.extend([str(digit_count), prev_digit])
                prev_digit = digit
                digit_count = 1
        # add delimiter
        next_seq.append("$")
        return self.next_sequence(n - 1, next_seq)

    def count_and_say_(self, n: int) -> str:
        """
        Approach: Regular Expression
        :param n:
        :return:
        """

        import re

        curr_seq = "1"
        pattern = r"((.)\2*)"

        for i in range(n - 1):
            next_seq = []
            for g1, g2 in re.findall(pattern, curr_seq):
                # append pair of <count, digit>
                next_seq.append(str(len(g1)))
                next_seq.append(g2)
            # next iteration
            curr_seq = "".join(next_seq)
        return curr_seq


if __name__ == "__main__":
    number = Number()
    print(number.count_and_say(4))
    print(number.count_and_say_(4))