from typing import List


class Parentheses:

    def generate(self, n: int) -> List[str]:
        """
        Approach: Back Tracking
        Time Complexity: O(4^n/ root(n))
        Space Complexity: O(4^n/ root(n))
        :param n:
        :return:
        """
        def back_track(s: str = "", left: int = 0, right: int = 0):
            # base cas
            if len(s) == 2*n:
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
    print(parentheses.generate(4))
    print(parentheses.generate(3))
    print(parentheses.generate(2))