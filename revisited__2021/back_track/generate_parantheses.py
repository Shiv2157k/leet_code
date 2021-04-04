from typing import List


class Parentheses:

    def generate(self, n: int) -> List[str]:
        """
        Approach: Back tracking
        Time Complexity: O(4^n / sqrt(n))
        Space Complexity: O(4^n / sqrt(n))
        :param n:
        :return:
        """

        def back_track(s: str = "", left: int = 0, right: int = 0):

            if len(s) == 2 * n:
                output.append(s)
                return  # back track
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
    print(parentheses.generate(2))