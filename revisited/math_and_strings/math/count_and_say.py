from typing import List


class Pattern:

    def count_n_say(self, num: int) -> str:
        """
        Approach: Using regular expression
        Time Complexity: O(2^n)
        Space Complexity: O(2^n - 1)
        :param num:
        :return:
        """
        import re
        curr_seq = "1"
        pattern = r"((.)\2*)"

        for n in range(num - 1):
            next_seq = []
            for g1, g2 in re.findall(pattern, curr_seq):
                # append the pair of <count, digit>
                next_seq.append(str(len(g1)))
                next_seq.append(g2)
            # prepare for next iteration
            curr_seq = "".join(next_seq)
        return curr_seq

    def __next_sequence(self, n: int, prev_seq: List[str]):
        """
        Recursion Method
        :param n:
        :param prev_seq:
        :return:
        """
        # base case
        if n == 1:
            # return everything ignoring the de-limiter
            return prev_seq[:-1]
        # to build the next sequence
        next_seq = []
        # previous digit is the 1st index value from the previous sequence
        prev_digit = prev_seq[0]
        # initial digit count
        digit_count = 1
        for digit in prev_seq[1:]:
            if digit == prev_digit:
                digit_count += 1
            else:  # reached the end of subsequence
                next_seq.extend([str(digit_count), prev_digit])
                prev_digit = digit
                digit_count = 1

        # add the de-limiter
        next_seq.append("$")
        return self.__next_sequence(n - 1, next_seq)

    def count_and_say(self, num: int) -> str:
        """
        Approach: Recursion
        Time Complexity: O(2^n)
        Space Complexity: O(2^n-1)
        :param num:
        :return:
        """
        return "".join(self.__next_sequence(num, ["1", "$"]))


if __name__ == "__main__":
    patterns = Pattern()
    print(patterns.count_and_say(4))
    print(patterns.count_and_say(5))
    p = Pattern()
    print(p.count_n_say(4))
    print(p.count_n_say(5))