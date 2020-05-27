from typing import List


class CountAndSay:

    def count_and_say_(self, n: int) -> str:
        """
        Approach: Recursion
        :param n:
        :return:
        """
        return ''.join(self.next_sequence(n, ['1', 'E']))

    def next_sequence(self, n: int, seq: List[str]):

        if n == 1:
            return seq[:-1]

        prev_digit, digit_cnt, next_seq = seq[0], 1, []
        for digit in seq[1:]:
            if digit == prev_digit:
                digit_cnt += 1
            else:
                next_seq.extend([str(digit_cnt), prev_digit])
                prev_digit = digit
                digit_cnt = 1
        next_seq.append('E')
        return self.next_sequence(n - 1, next_seq)

    def count_and_say(self, n: int) -> str:
        """
        Approach: Using regex pattern.
        :param n:
        :return:
        """

        from re import findall

        curr_seq = '1'
        """
        "(.)" -> this is a group that contains a single character that could be of anything.
        "[]" -> this part refers to second group (i.e., (.)) that we define.
        "((.)\2*" -> the outer bracket defines the scope of first group, which contains
                     repetitive appearance of the second group above.
        """
        pattern = r'((.)\2*)'

        for i in range(n - 1):
            next_seq = []
            for count, digit in findall(pattern, curr_seq):
                next_seq.extend([str(len(count)), digit])
            curr_seq = ''.join(next_seq)
        return curr_seq


if __name__ == "__main__":

    cs = CountAndSay()
    print(cs.count_and_say_(4))
    print(cs.count_and_say(4))