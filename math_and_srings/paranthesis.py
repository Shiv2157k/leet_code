from typing import List


class Parenthesis:

    def generate_combinations(self, num: int) -> List[str]:
        """
        Approach: Back tracking
        Time Complexity: O(4^n / sqrt(n))
        Space Complexity: O(4^n / sqrt(n))
        :param num:
        :return:
        """

        def back_track(string="", left=0, right=0):

            # Base Case
            if len(string) == 2 * num:
                combinations.append(string)

            if left < num:
                back_track(string + "(", left + 1, right)
            if right < left:
                back_track(string + ")", left, right + 1)

        if num == 0:
            return [""]
        combinations = []
        back_track()
        return combinations

    def generate_combinations_(self, num: int) -> List[str]:
        """
        Approach: Closure Number
        Time Complexity: O(4^n / sqrt(n))
        :param num:
        :return:
        """

        if num == 0:
            return [""]
        combinations = []
        for index in range(num):
            for left in self.generate_combinations_(index):
                for right in self.generate_combinations_(num - 1 - index):
                    combinations.append("({}){}".format(left, right))
        return combinations


if __name__ == "__main__":

    parenthesis = Parenthesis()
    print(parenthesis.generate_combinations(3))
    print(parenthesis.generate_combinations_(3))
