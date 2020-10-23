from typing import List


class Parentheses:

    def generates(self, n: int) -> List[str]:
        """
        Approach: Closure
        Time Complexity: O(4^n/root(n))
        Space Complexity: O(4^n/root(n))
        :param n:
        :return:
        """
        if n == 0:
            return [""]
        output = []
        for c in range(n):
            for left in self.generates(c):
                for right in self.generates(n - 1 - c):
                    output.append("({}){}".format(left, right))
        return output

    def generate(self, n: int) -> List[str]:
        """
        Approach: Back tracking
        Time Complexity: O(4^n/root(n))
        Space Complexity: O(4^n/root(n))
        :param n:
        :return:
        """

        def back_track(s="", left=0, right=0):

            # base case
            if len(s) == n * 2:
                output.append(s)
                return
            if left < n:
                back_track(s + "(", left + 1, right)
            if right < left:
                back_track(s + ")", left, right + 1)

        output = []
        back_track()
        return output


if __name__ == "__main__":
    parentheses = Parentheses()
    print(parentheses.generate(3))

    brackets = Parentheses()
    print(brackets.generates(3))