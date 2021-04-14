from typing import List
from sortedcontainers import SortedList


class Teams:

    def calculate_low_high(self, soldiers: "SortedList", rating):

        low = soldiers.bisect_left(rating)
        high = len(soldiers) - low
        return low, high

    def total_formed_(self, ratings: List[int]) -> int:
        """
        Approach: Using SortedList
        Time Complexity: O(N log N)
        Space Complexity: O(N)
        :param ratings:
        :return:
        """
        total_teams = 0

        left = SortedList()
        right = SortedList(ratings)

        for rating in ratings:
            right.remove(rating)

            lower_left, higher_left = self.calculate_low_high(left, rating)
            lower_right, higher_right = self.calculate_low_high(right, rating)
            total_teams += lower_left * higher_right + lower_right * higher_left
            left.add(rating)
        return total_teams

    def total_formed(self, ratings: List[int]) -> int:
        """
        Approach: Primitive Nested Loops with 4 counting variables
        Time Complexity: O(N^2)
        Space Complexity: O(1)
        Intuition:
        ---------
        Case 1:
        a < b < c
        lol * hir
        Case 2:
        a > b > c
        hil * lor
        Formulae :
        teams = lol * hir + hil * lor
        :param rating:
        :return:
        """
        if not ratings:
            return 0

        total_teams = 0

        for pivot in range(1, len(ratings) - 1):
            mid_val = ratings[pivot]

            lower_left = higher_right = 0
            lower_right = higher_left = 0

            # case 1: a < b < c
            for i in range(pivot):
                if ratings[i] < mid_val:
                    lower_left += 1
                else:
                    higher_right += 1
            # case 2: a > b > c
            for i in range(pivot + 1, len(ratings) - 1):
                if ratings[i] < mid_val:
                    lower_right += 1
                else:
                    higher_left += 1
            # make the calculation
            total_teams += lower_left * higher_right + lower_right * higher_left
        return total_teams


if __name__ == "__main__":
    teams = Teams()
    print(teams.total_formed([2, 5, 3, 4, 1]))
    print(teams.total_formed_([2, 5, 3, 4, 1]))